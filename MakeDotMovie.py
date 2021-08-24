import cv2

filepath = 'pict.mp4'
cap = cv2.VideoCapture(filepath)

#フレームレート(1フレームの時間単位はミリ秒)の取得
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
size = (60, 40) # 動画の画面サイズ

fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # ファイル形式(ここではmp4)
writer = cv2.VideoWriter('outtest.mp4', fmt, frame_rate, size, isColor=False) # ライター作成


# cv2.VideoWriter(filename, fmt, framerate, frameSize[, isColor=False])

while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    if not ret:
        break  # 映像取得に失敗

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, frame = cv2.threshold(frame, 10, 255, cv2.THRESH_BINARY)
    frame = cv2.resize(frame, dsize=(60, 40))
    frame = cv2.bitwise_not(frame)

    writer.write(frame) # 画像を1フレーム分として書き込み
    # cv2.imshow('Frame', frame)
    print("書き込み中")
    cv2.waitKey(1)

writer.release() # ファイルを閉じる
# cv2.destroyAllWindows()
