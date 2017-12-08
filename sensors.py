import stdio.h
import RoboPiLib.h
def LEFT_BUMPER = 0
def RIGHT_BUMPER = 0
def PRESSED = 0
int main(int argc, char *argv[]) {
    RoboPiInt("/dev/ttyAMA0",115200);
    pinMode(LEFT_BUMPER, INPUT);
    pinMode(RIGHT_BUMPER, INPUT);

    while (1) {
        if(digitalRead(LEFT_BUMPER) == PRESSED)
            puts("Left Bumper Pressed");
        if(digitalRead(RIGHT_BUMPER) == PRESSED)
            puts("Right Bumper Pressed");
        sleep(1); // only check once per second
    }
}
