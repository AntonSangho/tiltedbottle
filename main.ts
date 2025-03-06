let tilt = 0
// 초기 상태 - 두 LED 모두 꺼짐
pins.digitalWritePin(DigitalPin.P1, 0)
pins.digitalWritePin(DigitalPin.P2, 0)
// 반응성 조절을 위한 대기 시간
basic.forever(function () {
    // x축 가속도 값 읽기 (기울기)
    tilt = input.acceleration(Dimension.X)
    // 좌우 기울기에 따라 LED 제어
    if (tilt < -200) {
        // 왼쪽으로 기울임
        pins.digitalWritePin(DigitalPin.P1, 1)
        // P1 LED 켜기
        pins.digitalWritePin(DigitalPin.P2, 0)
    } else if (tilt > 200) {
        // P2 LED 끄기
        // 오른쪽으로 기울임
        pins.digitalWritePin(DigitalPin.P1, 0)
        // P1 LED 끄기
        pins.digitalWritePin(DigitalPin.P2, 1)
    } else {
        // P2 LED 켜기
        // 평평한 상태
        // 기울기가 충분하지 않으면 두 LED 모두 끄기
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    if (input.buttonIsPressed(Button.A)) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        // P2 LED 켜기
        // 평평한 상태
        // 기울기가 충분하지 않으면 두 LED 모두 끄기
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    if (input.buttonIsPressed(Button.B)) {
        pins.digitalWritePin(DigitalPin.P2, 1)
    } else {
        // P2 LED 켜기
        // 평평한 상태
        // 기울기가 충분하지 않으면 두 LED 모두 끄기
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    basic.pause(100)
})
