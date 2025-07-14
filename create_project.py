import os
import sys

template = '''
import cv2

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Kamera açılamadı.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
'''

def create_project(project_name):
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        print(f"📁 Klasör oluşturuldu: {project_name}")
    else:
        print("⚠️ Bu isimde bir klasör zaten var.")
        return

    with open(os.path.join(project_name, "main.py"), "w") as f:
        f.write(template)

    with open(os.path.join(project_name, "requirements.txt"), "w") as f:
        f.write("opencv-python\n")

    print("✅ Proje başarıyla oluşturuldu!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python create_project.py proje_adi")
    else:
        create_project(sys.argv[1])
