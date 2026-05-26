// Dada uma seqüência de n números, imprimi-la na ordem inversa à da leitura

#include <stdio.h>

int array[] = {1, 2, 3};

int main()
{

    int len = sizeof(array) / sizeof(array[0]);

    int newArray[3];

    for (int i = 0; i < len; i++) {
        newArray[i] = array[len - 1 - i];
    }

    for (int j = 0; j < len; j++) {
        printf("%d", newArray[j]);
    }
    
    return 0;
}