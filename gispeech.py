import random
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QRect
import nltk
import speech_recognition as sr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyQt5.QtCore import Qt

responses = {
    "What are the admission requirements for your college?": ["To be considered for admission, you will need to submit an application, your official high school Transfer Certificate, and your SSLC or HSC scores. For further details contact our Management [Enter management’s contact details]."],
            "What is the application deadline?": ["The application deadline is [insert deadline date here]. Please make sure to submit your application before this date."],
            "How do I apply to your college?": ["You can apply to our college online through our website. Just go to [insert college website here] and follow the instructions to submit your application."],
            "Is there an application fee?": ["Yes, there is a Rs. 1000 application fee. You can pay this fee online when you submit your application."],
            "Can I apply for scholarships?": ["Yes, you can apply for scholarships. Make sure to submit your family’s Income certificate and other required proofs by the priority deadline to maximize your scholarship eligibility. For further details contact out Management [Enter management’s contact details]."],
            "What majors does your college offer?": ["We offer a wide variety of majors, including [insert list of majors here]. You can find more information about our majors on our website."],
            "How many students are enrolled at your college?": ["We currently have [insert number of students here] enrolled at our college."],
            "What is the student-to-faculty ratio?": ["Our student-to-faculty ratio is [insert ratio here]. This means that our classes are built up in a way so that you will have plenty of opportunities to interact with your professors. "],
            "What is the average class size?": ["The average class size is [insert number of students here]. This means that you will have a personalized learning experience and plenty of opportunities to participate in class."],
            "What is the campus like?": ["Our campus is [insert description of campus here]. We have beautiful grounds, modern facilities, and plenty of opportunities for students to get involved in campus life."],
            "What kind of student organizations are there?": ["We have a variety of student organizations on campus, including NSS, NCC, Rotaract Club, Pattarai, Turbonites, and many more. You can find more information about these organizations on our website."],
            "What is the cost of tuition?": ["The cost of tuition for one year is [insert cost of tuition here]. This does not include room and board or other fees."],
            "What is the acceptance rate?": ["Our acceptance rate is [insert acceptance rate here]. This means that we receive a large number of applications, but we are still able to admit a significant number of students each year."],
            "What is the graduation rate?": ["Our graduation rate is 96.3%. This means that a high percentage of our students are able to complete their degree programs and earn their degrees."],
            "What kind of financial aid is available?": ["We offer a variety of financial aid options, including grants, scholarships, loans, and work-study programs. You can find more information about these options on our website."],
            "Can I schedule a campus tour?": ["Yes, you can schedule a campus tour through our website. Just go to [insert website here] and follow the instructions to schedule your tour."],
            "What kind of sports teams do you have?": ["We have a variety of sports teams on campus, including BasketBall, Football, Cricket, Volleyball, Hockey, Tennis, Handball, Table tennis, Badminton, Chess and Athletics. You can find more information about our sports teams on our website."],
            "Can you tell me about the admission requirements?": ["Please visit our webiste for admission related requirements "],
            "What is the application deadline for this year?": ["The application deadline for this year is May 1st."],
            "Is there an application fee?": ["Yes, the application fee is Rs 1000 for Management Quota."],
            "Can I apply online?": ["Yes, you can apply online by visiting our website."],
            "Hi": ["Hi there! How can i assist you?"],
            "Hello": ["Hello! How can i assist you?"],
            "Can I apply for financial aid?": ["Yes, you can apply for financial aid by submitting the required proofs. For further details contact out Management [Enter management’s contact details]."],
            "Can I transfer credits from another college?": ["Yes, you can transfer credits from another college as long as they meet our transfer credit requirements."],
            "What are the minimum GPA requirements?": ["The minimum GPA requirement is a 6.5 on a 10.0 scale."],
            "Can you tell me about campus life?": ["Yes, we have a variety of clubs, organizations, and events on campus. We also have a gym, dining hall, and housing options."],
            "Is there an honors program?": ["Yes, we have an honors program for qualified students."],
            "Can you tell me about the application process?": ["Sure, the application process involves submitting your transcripts, test scores, and other necessary documents. For further details contact out Management [Enter management’s contact details]."],
            "What is the minimum HSC 12th score required?": ["The minimum HSC score required is 70 on the 100 scale. For further details contact out Management [Enter management’s contact details]."],
            "Can I apply as a transfer student?": ["Yes, you can apply as a transfer student. For further details contact out Management [Enter management’s contact details]."],
            "How do I know if my application has been received?": ["You will receive a confirmation email once we have received your application."],
            "Can I apply for scholarships?": ["Yes, you can apply for scholarships by visiting our website. For further details contact out Management [Enter management’s contact details]."],
            "Can you tell me about the tuition fees?": ["Sure, the tuition fees vary depending on the program you choose. Please visit our website for more information. For further details contact out Management [Enter management’s contact details]."],
            "Can I apply for an early decision?": ["Yes, you can apply for an early decision. For further details contact out Management [Enter management’s contact details]."],
            "Is there an interview process?": ["Yes, there is an interview process for some programs. Regular updates about that will be sent to you mail once you complete the application process."],
            "What is the acceptance rate?": ["The acceptance rate varies depending on the program you choose."],
            "Can I schedule a campus tour?": ["Yes, you can schedule a campus tour by visiting our website."],
            "Can I apply for a specific dorm room?": ["No, we cannot guarantee specific dorm rooms."],
            "Is there a meal plan?": ["Yes, there is a meal plan available for Hostel students."],
            "Can you tell me about the study abroad programs?": ["Sure, we have a variety of study abroad programs along with internship offers available for students. For further details contact out Management [Enter management’s contact details]."],
            "Is there a placement test?": ["Yes, there may"],
            "what about cutoff": ["The cutoff requied varies in accordance with the choice of the student's departmemt and cast. For further more and accurate details look on the CUTOFF INSIGHTS in the welcome page"],
            "what about placements": ["The placements in LICET are top notch and the placement trainings will be given right from the 2nd year. The range lies between 4LPA to 12LPA in accordance with the student's skillsets. For further details, look on the PLACEMENT INSIGHTS in the welcome page."],
            "Are there any clubs or organizations on campus?": ["Yes, we have over 30 clubs and organizations on campus."],
            "Can I start my own club?": ["Yes, you can start your own club. You will need to complete a club application and meet certain requirements."],
            "What kind of research opportunities are available?": ["We offer various research opportunities for undergraduate and graduate students."],
            "Is there a library on campus?": ["Yes, we have a library on campus with a wide range of resources. You can have a virtual experience of our library by scheduling a virtual tour."],
            "What kind of campus safety measures are in place?": ["We have a strict campus security system and various safety measures in place to ensure the safety of our students."],
            "Can I bring a car to campus?": ["Yes, you can bring a car to campus, but you will need to purchase a parking permit."],
            "What kind of food options are available on campus?": ["We have various dining options on campus such as a cafeteria, canteen, and cafes."],
            "Can I request special accommodations for my disability?": ["Yes, we provide accommodations for students with disabilities. You can request accommodations through our disability services office."],
            "Are there any language requirements for international students?": ["Yes, international students are required to demonstrate proficiency in English. You can find more information on our website."],
            "What kind of support services are available for students?": ["We offer various support services such as tutoring, counseling, and career services."],
            "Can I apply for an internship?": ["Yes, we offer various internship opportunities for students."],
            "What kind of jobs are available on campus?": ["We offer various part-time jobs on campus such as working at the bookstore or in the cafeteria."],
            "What kind of technology resources are available on campus?": ["We have various technology resources such as computer labs, Wi-Fi, and software programs. You can have a virtual experience of our facilities by scheduling a virtual tour."],
            "How can I get involved in community service?": ["We offer various community service opportunities for students through our volunteer center."],
            "Can I take classes at other colleges or universities?": ["Yes, we have agreements with other colleges and universities that allow students to take classes at their institutions."],
            "Can I get academic credit for my internship?": ["Yes, you can get academic credit for your internship through our internship program."],
            "How can I get involved in undergraduate research?": ["You can get involved in undergraduate research by contacting faculty members in your department or through our undergraduate research program."],
            "What kind of resources are available for graduate students?": ["We offer various resources for graduate students such as research funding, assistantships, and professional development opportunities."],
            "How can I access the career services office?": [" You can access the career services office through our website or by visiting their office on campus."],
            "What kind of academic support services are available for students?": ["We offer various academic support services such as tutoring, study groups, mentoring and academic advising."],
            "User: How can I get involved in student government?": ["You can get involved in student government by running for a student government position or joining a student government organization."],
            "What is the average class size?": ["The average class size is about 60 students."],
            "What about hostel": ["The hostel facilities are very great in LICET. Hoatel accomodation process can be started along with or right after you have completed the Admission process (offline). You can have a view on our hostel and its facilities by looking on to our website. For further more details you can contact the LICET Management or Mr. Suman sir (Hostel Warden contact details)"],
            "What kind of sports teams does the college have?": ["We have a variety of sports teams, including BasketBall, Football, Cricket, Volleyball, Hockey, Tennis, Handball, Table tennis, Badminton, Chess and Athletics. You can find more information about our sports teams on our website."],
            "Can I get academic credit for studying abroad?": ["Yes, you can get academic credit for studying abroad through our study abroad program."],
            "Can I bring a pet to campus?": ["Unfortunately, pets are not allowed on campus."],
            "Can I change my major?": ["Yes, you can change your major by speaking with your academic advisor within the initial phase of your academic journey."],
            "What kind of religious organizations are on campus?": ["Our institution is a Christian Institution with a wide range of students studying in our institution and one of our main motto is Holistic Formation. "],
            "What kind of recreational activities are available on campus?": ["We offer various recreational activities such as Seminars, outdoor programs, and more."],
            "How can I get involved in student clubs and organizations?": ["You can get involved in student clubs and organizations by attending club fairs, browsing our online directory, or contacting the organization directly."],
            "Is there a career center on campus?": ["Yes, we have a career center on campus that offers career counseling, job search assistance, and more."],
            "What kind of health services are available on campus?": ["We offer various health services on campus such as a health clinic, counseling services, and more."],
            "What kind of financial aid is available?": ["We offer various types of financial aid such as scholarships, grants, loans, and work-study programs."],
            "Can I get credit for my previous college courses?": ["Yes, you may be able to transfer credit for your previous college courses. You will need to have your transcripts evaluated by our transfer credit office."],
            "Is there a student handbook or code of conduct?": ["Yes, we have a student handbook and code of conduct that outlines our policies and procedures for students."],
            "Can I get involved in undergraduate research as a freshman?": ["Yes, you can get involved in undergraduate research as a freshman. You can contact faculty members in your department or apply for our undergraduate research program."],
            "What kind of student support services are available?": ["We offer various student support services such as Scholarships, Mentoring, Counseling and many more."],
            "What are the requirements for admission?": ["The requirements for admission vary by program and degree level. You can find more information on our website or by contacting our admissions office."],
            "Can I visit the campus before I apply?": ["Yes, we offer campus tours and information sessions for prospective students. You can even experience a virtual campus tour and you can find more information on our website or by contacting our admissions office."],
            "What is the tuition cost per semester?": ["The tuition cost per semester varies by program and degree level. You can find more information on our website or by contacting our financial aid office."],
            "Can I get a waiver for the application fee?": ["We do offer application fee waivers for eligible students. You can find more information on our website or by contacting our admissions office."],
            "What kind of extracurricular activities are available on campus?": ["We offer a variety of extracurricular activities such as student clubs and organizations, sports teams, and volunteer opportunities."],
            "How can I apply for scholarships?": ["You can apply for scholarships by filling out the scholarship application on our website or by contacting our financial aid office."],
            "Is there a study abroad fair on campus?": ["Yes, we do have a study abroad fair on campus where you can learn more about our study abroad programs and opportunities."],
            "Can I take a gap year before starting college?": ["Yes, you can take a gap year before starting college. You can find more information on our website or by contacting our admissions office."],
            "What kind of student housing is available off campus?": ["We do not have any affiliated off-campus housing, but there are various housing options available near campus."],
            "What kind of internship opportunities are available?": ["We offer various internship opportunities through our career center and departmental programs."],
            "Can I transfer from another college?": ["Yes, you can transfer from another college. You will need to submit official transcripts and meet our transfer admission requirements."],
            "What kind of academic support services are available?": ["We offer various academic support services such as tutoring, academic coaching, and study skills workshops."],
            "What kind of job placement services are available?": ["We offer job placement services through our career center, including job search assistance, placement training, resume reviews, and career fairs."],
            "Can I apply as an international student?": ["Yes, we do accept international students. You will need to submit additional documentation and meet our international admission requirements."],
            "Can I apply for a specific major within the college?": ["Yes, you can apply for a specific major within the college. However, some majors may have additional admission requirements or prerequisites."],
            "Can I take classes online?": ["No, we did offer online classes during COVID times but it is not currently under practice. You can find more information on our website or by contacting our online learning department"],
            "What are the college hours?": ["Generally the college hours are from 08:00 AM to 04:00 PM but it could vary accordingly on certain days."],
            "What is the average class size?": ["The average class size varies by program and course. Most classrooms are of similar size except laboratories and some other classrooms. However, we strive to maintain small class sizes to provide students with personalized attention and engagement with the professors."],
            "How can I get involved in community service projects?": ["You can get involved in community service projects through our service-learning program, volunteer center, or student clubs and organizations."],
            "Is there an honors program?": ["Yes, we have an honors program for academically talented and motivated students. You can find more information on our website or by contacting our honors program director."],
            "Can I take courses at other colleges and universities while enrolled?": ["Yes, you can take courses at other colleges and universities while enrolled. However, you will need to meet our transfer credit policies and obtain approval from your academic advisor."],
            "How can I get a transcript of my courses and grades?": ["You can request an official transcript of your courses and grades through our registrar's office. You can find more information on our website or by contacting the registrar's office."],
            "What kind of facilities and equipment are available for students to use?": ["We have various facilities and equipment available for student use, such as computer labs, science labs, music studios, and libraries and many more."],
            "Can I change my major after enrolling?": ["Yes, you can change your major after enrolling. However, you will need to meet the admission requirements and prerequisites for the new major."],
            "Can I take a course pass/fail instead of for a letter grade?": ["Yes, you can take a course pass/fail instead of for a letter grade. However, there may be limitations and restrictions on which courses are eligible for this grading option. You can find more information on our website or by contacting your academic advisor."],
            "what is student life like": ["At our college, student life is vibrant and diverse. We have many clubs, organizations, and sports teams for students to get involved in, as well as numerous social events throughout the year. We also have a strong focus on community service and encourage our students to give back to the community.",
                                  "Student life at our college is about more than just academics. We offer a variety of extracurricular activities, clubs, and organizations to help students connect with others who share their interests. We also believe in the importance of community service and offer many opportunities for students to give back."],
            "exit": ["Thank you for your interest in our college. Have a great day!", "Goodbye! We hope to hear from you soon."],
            "bye": ["Thank you for your interest in our college. Have a great day!", "Goodbye! We hope to hear from you soon."]
}

class ChatBot(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 800)
        self.setStyleSheet("border: 1px solid black; font-size:20px; padding: 5px; color:#000000; font-weight:italics; background-image: url('C:/Users/karun/OneDrive/Desktop/py/image12.png'); background-repeat: no-repeat; background-position: center; background-attachment: fixed;")


        # Create a label and text box for displaying chatbot responses
        self.response_label = QLabel(self)
        self.response_label.setText("Welcome to LICET Admission Enquiry Bot")
        self.response_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.response_label.setAlignment(Qt.AlignTop)
        self.response_text = QTextEdit(self)
        self.response_text.setReadOnly(True)

        # Create a button for activating speech recognition
        self.recognize_button = QPushButton("SPEAK NOW", self)
        self.recognize_button.clicked.connect(self.recognize_speech)
        self.recognize_button.setStyleSheet("background-color:#00cc00;")
        self.recognize_button.setStyleSheet("""
            QPushButton {
                background-color: #00cc00;
                color: black;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            
            QPushButton:hover {
                background-color: #00b300;
            }
        """)

        # Create a button for closing the chatbot window
        self.close_button = QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("background-image: url('');")
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        
        

        # Create a scroll area for the chatbot responses
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.response_text)
        self.scroll_area.setStyleSheet("background-image: url('');")
        self.scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background-color: #f2f2f2;
                width: 10px;
                margin: 0px 0 0px 0;
            }

            QScrollBar::handle:vertical {
                background-color: #888;
                min-height: 50px;
            }

            QScrollBar::add-line:vertical {
                background: none;
            }

            QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar {
                background: #FFFFFF;
            }
        """)
        

        # Set up the layout for the GUI
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.response_label)
        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.recognize_button)
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        self.show()

    
    def process_input(self, input_text):
        # Tokenize the input text
        input_tokens = nltk.word_tokenize(input_text.lower())
        
        # Get the TF-IDF vectors for the possible user inputs and the user input
        vectorizer = TfidfVectorizer()
        vectorizer.fit(list(responses.keys()) + input_tokens)
        input_vector = vectorizer.transform(input_tokens)
        response_vectors = vectorizer.transform(responses.keys())
        
        # Calculate the cosine similarities between the input vector and each response vector
        similarities = cosine_similarity(input_vector, response_vectors)
        
        # Get the index of the most similar response
        response_index = similarities.argmax()
        
        # Return the response
        return random.choice(responses[list(responses.keys())[response_index]])
    
    def recognize_speech(self):
        # Initialize the recognizer and microphone
        r = sr.Recognizer()
        mic = sr.Microphone()
        
        # Adjust for ambient noise
        with mic as source:
            r.adjust_for_ambient_noise(source)
        
        # Prompt the user to speak and recognize their speech
        with mic as source:
            self.response_text.append("Speak now!")
            audio = r.listen(source)
        
        try:
            # Convert speech to text
            text = r.recognize_google(audio)
            response = self.process_input(text)
            self.response_text.append("You: " + text)
            self.response_text.append("Chatbot: " + response)
        except sr.UnknownValueError:
            # If the speech cannot be recognized, ask the user to repeat
            self.response_text.append("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            # If there is an error with the speech recognition API, notify the user
            self.response_text.append("Could not request results from speech recognition service; {0}".format(e))

if __name__ == "__main__":
    app = QApplication([])
    chatbot = ChatBot()
    app.exec_()
