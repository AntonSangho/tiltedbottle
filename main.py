strip = neopixel.create(DigitalPin.P1, 8, NeoPixelMode.RGB)
strip.clear()
strip.show()

# 현재 LED 위치 (0-7)
current_position = 3  # 중앙에서 시작

def on_forever():
    global current_position
    # x축 가속도 값 읽기 (기울기)
    tilt = input.acceleration(Dimension.X)
    
    # 가속도 값에 따른 위치 조정
    if tilt > 200:  # 오른쪽으로 기울임
        current_position = current_position + 1
    elif tilt < -200:  # 왼쪽으로 기울임
        current_position = current_position - 1
    
    # 범위 제한 (0-7)
    if current_position < 0:
        current_position = 0
    if current_position > 7:
        current_position = 7
    
    # 모든 LED 초기화
    strip.clear()
    
    # 현재 위치의 LED만 켜기
    strip.set_pixel_color(current_position, neopixel.colors(NeoPixelColors.WHITE))
    
    strip.show()
    basic.pause(200)  # 반응성 조절을 위한 대기 시간
    
basic.forever(on_forever)