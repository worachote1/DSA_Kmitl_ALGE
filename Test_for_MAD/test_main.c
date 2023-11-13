unint8_t led0 = 0; // pin 0
unint8_t led1 = 0; // pin 7
unint8_t led2 = 0; // pin 14
while (1)
  {
      //update led counter
    led0 += 1;
    if (led0 > 1)
    {
        led0 = 0;
        led1 += 1;

        if (led1 > 1)
        {
            led1 = 0;
            led2 += 1;

            if (led2 > 1)
                led2 = 0;
        }
    }
      
      HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0, GPIO_PIN_SET);
      HAL_Delay(300);
      HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0, GPIO_PIN_RESET);
      HAL_Delay(300);
      HAL_GPIO_WritePin(GPIOB, GPIO_PIN_7, GPIO_PIN_SET);
      HAL_Delay(300);
      HAL_GPIO_WritePin(GPIOB, GPIO_PIN_7, GPIO_PIN_RESET);
      HAL_Delay(300);
      HAL_GPIO_WritePin(GPIOB, GPIO_PIN_14, GPIO_PIN_SET);
      HAL_Delay(300);
      HAL_GPIO_WritePin(GPIOB, GPIO_PIN_14, GPIO_PIN_RESET);
      HAL_Delay(300);
  }