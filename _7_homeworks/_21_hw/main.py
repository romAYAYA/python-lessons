import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMessageBox
import threading
import requests
import os


class SavePosts(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Save Posts')
        self.setGeometry(100, 100, 400, 150)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Enter the number of posts to save:")
        self.layout.addWidget(self.label)

        self.post_count_input = QLineEdit()
        self.layout.addWidget(self.post_count_input)

        self.save_button = QPushButton("Save Posts")
        self.save_button.clicked.connect(self.save_posts)
        self.layout.addWidget(self.save_button)

    def save_posts(self):
        post_count = self.post_count_input.text()

        try:
            post_count = int(post_count)
            if post_count <= 0:
                raise Exception()
        except Exception as err:
            QMessageBox.critical(self, "Error", "Please enter a valid positive integer.")
            return

        thread = threading.Thread(target=self.save_posts_thread, args=(post_count,))
        thread.start()

    def save_posts_thread(self, post_count):
        url = 'https://jsonplaceholder.typicode.com/posts'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                posts = response.json()

                os.makedirs('temp', exist_ok=True)

                for i, post in enumerate(posts[:post_count]):
                    with open(f'temp/post_{i + 1}.txt', 'w') as file:
                        file.write(f'Title: {post["title"]}\n')
                        file.write(f'Body: {post["body"]}\n')

                QMessageBox.information(self, 'Success', f'{post_count} posts saved successfully.')
            else:
                QMessageBox.critical(self, 'Error', 'Failed to fetch posts from the API.')
        except Exception as err:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(err)}')


def main():
    app = QApplication(sys.argv)
    window = SavePosts()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
