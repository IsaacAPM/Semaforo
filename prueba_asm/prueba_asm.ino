void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  asm volatile(
    ".INCLUDE \"/home/isaacapm/Arduino/prueba_asm/include/m2560def.inc\" \n\t"
    "LDI R20, 0x00 \n\t"
    "OUT DDRA, R20 \n\t"
    "LDI R21, 0xFF \n\t"
    "OUT PORTA, R21 \n\t"
    );
}
