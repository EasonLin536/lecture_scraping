# Lecture Scraping
scrap all courses of National Taiwan University and implement a simple search engine

## Usage
### Install packages
```bash
pip install -r requirements.txt
```

### Scrap all lectures
```bash
python3 src/lecture_scrap.py <semester> <output_fname>
```
`<semester>` should be in the form like `108-2`
`<output_fname>` file type should be `.xlsx`
example ```python3 src/lecture_scrap.py 108-2 results/all_lectures.xlsx```

### Search for lectures
```bash
python3 src/lecture_search.py [-de department] [-nu class_number] [-na class_name] [-te professor] [-ti time] [-ro room] [-re remark]
```
example ```python3 src/lecture_search.py -de 電機 -nu EE1 -na 電磁學一 -te 江衍偉 -ti <一>6,7,8,9 -ro 電二225 -re 兼通識```
type ```quit``` in terminal to quit the program