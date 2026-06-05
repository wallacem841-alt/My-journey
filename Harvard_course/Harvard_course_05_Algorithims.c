#include <stdio.h>
#include <string.h>

typedef struct {
    char *name;
    int height;  // Changed to int to store numerical height values
} wifu;

int main(void) {
    // Initialize an array of `wifu` structs
    wifu waifus[] = {
        // Genshin Impact
        {"Yae Miko", 170},
        {"Ganyu", 170},
        {"Raiden Shogun", 163},
        {"Hu Tao", 162},
        {"Eula", 170},
        
        // League of Legends
        {"Ahri", 158},
        {"Miss Fortune", 160},
        {"Lux", 163},
        {"Akali", 155},
        {"Jinx", 163},

        // Nikke: Goddess of Victory
        {"Scarlet", 163},
        {"Alice", 163},
        {"Privaty", 163},
        {"Harran", 163},
        {"Rapi", 163}
    };

    int size = sizeof(waifus) / sizeof(waifus[0]);

    for (int i = 0; i < size; i+=1){
        if (strcmp(waifus[i].name, "Lux") == 0){
            printf("Found %s her height is %dcm\n", waifus[i].name, waifus[i].height);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}