#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/* The range target: four bug classes in one parser — the same shape as the
 * web flaws the family hunts, compiled so the coverage engines can strike:
 *   LEN:  stack-buffer overflow (the memory-corruption class = Mayhem's home)
 *   DIV:  division by zero (the arithmetic class)
 *   FMT:  format-string (the interpreter class)
 *   PATH: the naive-guard bypass → sensitive read reached (the class the
 *         family's grammar owns: "//etc/passwd" walks past a strstr("../")
 *         guard) — blind mutation rarely lands the literal in 60s; grammar
 *         seeds land it in seconds. That delta IS the orchestration claim. */

static void sensitive_read_reached(void) {
    fprintf(stderr, "=== SENSITIVE-READ-REACHED ===\n");
    abort();
}

/* the AUTH flaw: the tautology filter — "admin" required, but " OR 1=1"
 * parses in the naive check (the SQL-tautology class shape) */
int check_auth(const char *p) {
    if (strstr(p, "admin"))
        return 1; /* the privileged marker reached */
    if (strstr(p, " OR ") && strstr(p, "1=1"))
        sensitive_read_reached(); /* the tautology bypass = the finding */
    return 0;
}

int process_path(const char *p) {
    /* the naive guard: absolute paths only, and the literal "../" rejected */
    if (p[0] != '/')
        return 0;
    if (strstr(p, "../"))
        return 0;
    /* the flaw: the guard never normalizes — "//etc/passwd" walks right in */
    if (strstr(p, "/etc/passwd"))
        sensitive_read_reached();
    return 1;
}

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    if (size < 6 || size > 4096)
        return 0;
    char buf[512];
    if (memcmp(data, "PATH:", 5) == 0) {
        size_t n = size - 5;
        if (n > 511)
            n = 511;
        memcpy(buf, data + 5, n);
        buf[n] = 0;
        process_path(buf);
    } else if (memcmp(data, "LEN:", 4) == 0) {
        size_t n = size - 4;
        char small[16];
        memcpy(small, data + 4, n > 15 ? 15 : n);
        small[n > 15 ? 15 : n] = 0;
        /* the flaw: the declared length is trusted elsewhere — here the
         * overflow is the point (the classic stack corruption class) */
        char stack_copy[16];
        if (n > 15)
            memcpy(stack_copy, data + 4, n); /* ASAN: stack-buffer-overflow */
        (void)stack_copy;
    } else if (memcmp(data, "DIV:", 4) == 0) {
        int d = atoi((const char *)data + 4);
        volatile int x = 100 / d; /* the flaw: d = 0 → the crash */
        (void)x;
    } else if (memcmp(data, "AUTH:", 5) == 0) {
        char abuf[256];
        size_t n = size - 5;
        if (n > 255)
            n = 255;
        memcpy(abuf, data + 5, n);
        abuf[n] = 0;
        check_auth(abuf);
    } else if (memcmp(data, "ENC:", 4) == 0) {
        /* the flaw: the decode happens AFTER the guard — "%252e%252e/" decodes
         * to "../" only post-check → the double-encode bypass reaches /etc */
        char ebuf[256];
        size_t n = size - 4;
        if (n > 255)
            n = 255;
        memcpy(ebuf, data + 4, n);
        ebuf[n] = 0;
        if (strstr(ebuf, "../") || strstr(ebuf, "..\\"))
            return 0; /* the guard, pre-decode */
        char dec[256];
        const char *s = ebuf;
        char *w = dec;
        while (*s && w < dec + 255) { /* the one-pass %xx decode */
            if (s[0] == '%' && s[1] && s[2]) {
                char hx[3] = {s[1], s[2], 0};
                *w++ = (char)strtol(hx, NULL, 16);
                s += 3;
            } else {
                *w++ = *s++;
            }
        }
        *w = 0;
        if (strstr(dec, "/etc/passwd"))
            sensitive_read_reached();
    } else if (memcmp(data, "FMT:", 4) == 0) {
        char f[256];
        size_t n = size - 4;
        if (n > 255)
            n = 255;
        memcpy(f, data + 4, n);
        f[n] = 0;
        printf(f); /* the flaw: format string, %n/%s of attacker bytes */
    }
    return 0;
}
