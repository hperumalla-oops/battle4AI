#include <stdio.h>
#include <stdlib.h>   // For rand() and srand()
#include <sys/time.h>
#include <cstring> // For gettimeofday()
#include <time.h>  

#define MAX 100

long timeee() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec * 1000000L + tv.tv_usec;
}


void topologicalSort(int graph[MAX][MAX], int n) {
    int in_degree[MAX] = {0};

    // Calculate in-degree of each node
    for (int col = 0; col < n; col++)
        for (int row = 0; row < n; row++)
            if (graph[row][col])
                in_degree[col]++;

    int count = 0;
    while (count < n) {
        int found = 0;
        for (int i = 0; i < n; i++) {
            if (in_degree[i] == 0) {
                printf("%d ", i);
                in_degree[i] = -1;  // Mark as deleted
                count++;
                found = 1;

                // Remove edges from this vertex
                for (int j = 0; j < n; j++) {
                    if (graph[i][j]) {
                        in_degree[j]--;
                    }
                }
                break;
            }
        }

        if (!found) {
            printf("\nCycle detected. Topological sort not possible.\n");
            return;
        }
    }
    printf("\n");
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // pivot
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            // swap arr[i] and arr[j]
            int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
        }
    }
    int temp = arr[i+1]; arr[i+1] = arr[high]; arr[high] = temp;
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

#define MAX_CHAR 256

void buildShiftTable(char pattern[], int m, int shiftTable[]) {
    for (int i = 0; i < MAX_CHAR; i++)
        shiftTable[i] = m;

    for (int i = 0; i < m - 1; i++)
        shiftTable[(unsigned char)pattern[i]] = m - 1 - i;
}

int horspoolSearch(char text[], char pattern[]) {
    int m = strlen(pattern);
    int n = strlen(text);
    int shiftTable[MAX_CHAR];
    buildShiftTable(pattern, m, shiftTable);

    int i = m - 1;

    while (i < n) {
        int k = 0;
        while (k < m && pattern[m - 1 - k] == text[i - k])
            k++;

        if (k == m) return i - m + 1;  // Match found

        i += shiftTable[(unsigned char)text[i]];
    }

    return -1;  // Not found
}

#define INF 99999

void floydWarshall(int graph[][MAX], int n) {
    int dist[MAX][MAX];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            dist[i][j] = graph[i][j];

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];

    // Display result
    printf("Shortest distance matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf("%7s", dist[i][j] == INF ? "INF" : (char[7]){0} + sprintf((char[7]){0}, "%d", dist[i][j]));
        printf("\n");
    }
}

int x[20];

int place(int k, int i) {
    int j;
    for (j = 1; j <= k - 1; j++) {
        if (x[j] == i || abs(x[j] - i) == abs(j - k))
            return 0;
    }
    return 1;
}

void printQueen(int n) {
    int i, j;
    static int count = 1;
    printf("\n\nSolution %d is - \n\n", count++);
    for (i = 1; i <= n; ++i)
        printf("\t%d", i);
    for (i = 1; i <= n; ++i) {
        printf("\n\n%d", i);
        for (j = 1; j <= n; ++j) {
            if (x[i] == j)
                printf("\tQ");
            else
                printf("\t-");
        }
    }
}

void NQueen(int k, int n) {
    int i;
    for (i = 1; i <= n; i++) {
        if (place(k, i)) {
            x[k] = i;
            if (k == n) {
                printQueen(n);
            } else {
                NQueen(k + 1, n);
            }
        }
    }
}

void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Temp arrays
    int L[n1], R[n2];

    // Copy data
    for (i = 0; i < n1; i++) L[i] = arr[left + i];
    for (j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    // Merge temp arrays
    i = 0; j = 0; k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }

    // Copy remaining
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        // Swap
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}


void TOH(int n, char source, char auxiliary, char destination) {
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", source, destination);
        return;
    }
    TOH(n - 1, source, destination, auxiliary);
    printf("Move disk %d from %c to %c\n", n, source, destination);
    TOH(n - 1, auxiliary, source, destination);
}



int main() {
    // // 1. Tower of Hanoi
    // printf("Tower of Hanoi:\n");
    // TOH(3, 'A', 'B', 'C');

    // // 2. Selection Sort
    // int arr1[] = {29, 10, 14, 37, 13};
    // int n1 = sizeof(arr1) / sizeof(arr1[0]);
    // selectionSort(arr1, n1);
    // printf("\nSelection Sorted: ");
    // for (int i = 0; i < n1; i++) printf("%d ", arr1[i]);

    // // 3. Merge Sort
    // int arr2[] = {38, 27, 43, 3, 9, 82, 10};
    // int n2 = sizeof(arr2) / sizeof(arr2[0]);
    // mergeSort(arr2, 0, n2 - 1);
    // printf("\nMerge Sorted: ");
    // for (int i = 0; i < n2; i++) printf("%d ", arr2[i]);

    // 4. Topological Sort
    int graph[MAX][MAX] = {
        {0, 1, 1, 0, 0},
        {0, 0, 0, 1, 0},
        {0, 0, 0, 1, 1},
        {0, 0, 0, 0, 1},
        {0, 0, 0, 0, 0}
    };
    printf("\nTopological Order: ");
    topologicalSort(graph, 5);

    // //5. N queens
    // printf("\nEnter the number of queens to be placed - ");
    // scanf("%d", &n);
    
    // if (n < 4) {
    //     printf("\nNo solutions possible for N < 4.\n");
    //     return 0;
    // }
    // NQueen(1, n);

    // //6. Call QuickSort
    // int arr[] = {10, 7, 8, 9, 1, 5};
    // int n = sizeof(arr) / sizeof(arr[0]);
    // quickSort(arr, 0, n - 1);

    // //7. Call Horspool
    // char text[] = "ababcabcabababd";
    // char pattern[] = "ababd";
    // int index = horspoolSearch(text, pattern);
    // printf("Pattern found at index %d\n", index);

    //8. Call Floyd-Warshall
    int graph2[MAX][MAX] = {
        {0, 5, INF, 10},
        {INF, 0, 3, INF},
        {INF, INF, 0, 1},
        {INF, INF, INF, 0}
    };
    floydWarshall(graph, 4);

    return 0;
}

