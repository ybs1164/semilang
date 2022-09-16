#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

typedef struct func {
    size_t nBytes;
    size_t nSize;
    void *(*f)();
    unsigned char args[1];
} Func;

Func * beginFunc(void (*f)(), int nSize, void *area) {
    Func *p = area;
    if (p) {
        p->nBytes = 0;
        p->nSize = nSize - sizeof(Func);
        p->f = f;
    }
    return p;
}

Func * pushDataFunc(Func *p, size_t size, ...) {
    if (p && p->nBytes + size < p->nSize) {
        va_list jj;

        va_start(jj, size);

        memcpy(p->args + p->nBytes, jj, size);
        p->nBytes += size;
        va_end(jj);
    }

    return p;
}

void * callFunc(Func *p) {
    if (p) {
        if ((p)->nBytes < 64) {
            struct {
                unsigned char x[64];
            } *px = (void *)p->args;
            return p->f(*px);
        } else {
            return p->f((void *)p->args);
        }
    }
}

#define PUSHDATA(cs,d) pushDataFunc((cs),sizeof(d),(d))

int damaged(int *hp, int damage) {
    *hp = *hp - damage;
    return *hp;
}

Func created_hp(int hp) {
    Func *f = beginFunc(damaged, 256, malloc(256));
    f = PUSHDATA(f, &hp);
    return *f;
}

int main(void) {
    Func *p = beginFunc(created_hp, 512, malloc(512));
    p = PUSHDATA(p, 68);
    p = callFunc(p);
    p = PUSHDATA(p, 10);
    printf("%d", callFunc(p));

    return 0;
}