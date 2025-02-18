#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#define GPIO_OUTPUT_IO 4
#define GPIO_OUTPUT_PIN_SEL (1ULL<<GPIO_OUTPUT_IO)

void app_main() {
    //zero-initialize the config structure.
    gpio_config_t io_conf = {};
    //disable interrupt
    io_conf.intr_type = GPIO_INTR_DISABLE;
    //set as output mode
    io_conf.mode = GPIO_MODE_OUTPUT;
    //bit mask of the pins that you want to set
    io_conf.pin_bit_mask = GPIO_OUTPUT_PIN_SEL;
    //disable pull-down mode
    io_conf.pull_down_en = 0;
    //disable pull-up mode
    io_conf.pull_up_en = 0;
    //configure GPIO with the given settings
    gpio_config(&io_conf);
    while(1) {
    printf("Led on \n");
    vTaskDelay(1000 / portTICK_PERIOD_MS);
    gpio_set_level(GPIO_OUTPUT_IO, 1);

    printf("Led off \n");
    vTaskDelay(500 / portTICK_PERIOD_MS);
    gpio_set_level(GPIO_OUTPUT_IO, 0);

    printf("Led on \n");
    vTaskDelay(250 / portTICK_PERIOD_MS);
    gpio_set_level(GPIO_OUTPUT_IO, 1);

    printf("Led off \n");
    vTaskDelay(750 / portTICK_PERIOD_MS);
    gpio_set_level(GPIO_OUTPUT_IO, 0);
    }
}
    
// Q:Ce rol are functia gpio config?
// A: Configure GPIO's Mode,pull-up,PullDown,IntrType
// Configureaza modul de intrare/iesire a pinilor si rezistentele pull-up pullDown

// Q: In codul exemplu, pinul GPIO4 este configurat ca iesire. Care sunt celelalte moduri ˆın care poate fi configurat un pin GPIO?
// A: Un pin mai poate fi configurat ca intrare, iesire, intrare-iesire etc
// GPIO_MODE_DISABLE, GPIO_MODE_INPUT, GPIO_MODE_OUTPUT, GPIO_MODE_OUTPUT_OD, GPIO_MODE_INPUT_OUTPUT_OD, GPIO_MODE_INPUT_OUTPUT

//Q: Explicati apelul vTaskDelay
//A: Intarzie un task pentru un anumit timp

//Q: De ce functia principala se numeste app main?
//A: 