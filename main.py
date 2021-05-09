from bs4 import BeautifulSoup
with open('index.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')

    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)

    course_carts = soup.find_all('div', class_='card')
    for courses in course_carts:
        course_name = courses.h5.text
        course_price = courses.a.text.split()[-1]
        print(f'{course_name} for {course_price}')
