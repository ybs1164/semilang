#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct node {
    void *data;
    char isMarked;
    struct node *next;
} Node;

Node *root;
Node *heapStart = NULL;
Node *heapEnd = NULL;

void HeapPush(Node *value) {
    if (heapStart == NULL) {
        heapStart = value;
    } else {
        heapEnd->next = value;
    }
    heapEnd = value;
}

void HeapRemove(Node *value) {
    Node *removed;

    removed = value;
    value = value->next;
    free(removed);
}

void RootPush(Node *value) {
    root->next = root;
    root = value;
}

Node *work;

void WorkPush(Node *value) {
    work->next = work;
    work = value;
}

void WorkPop() {
    Node *removed = work;
    work->next = work;
    free(removed);
}

void Mark() {
    while (work != NULL) {
        WorkPop();
        
    }
}

void MarkFromRoots() {
}

void Sweep(Node *start, Node *end) {

}

void Collect() {
    MarkFromRoots();
    Sweep(heapStart, heapEnd);
}

void* New(int size) {
    void* ref = malloc(size);
    if (ref == NULL) {
        Collect();
        ref = malloc(size);
        if (ref == NULL) {
            return NULL;
        }
    }
    return ref;
}

int main(void) {
    return 0;
}