from flask import Flask, render_template, request, url_for, Markup
import json
import requests

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
	r = requests.get('http://titanic.businessoptics.biz/survival/')

	s = json.loads(r.text)
	age_survival = []

	if request.method == 'GET':
		return render_template("index.html")

	if request.method == 'POST':

		if request.form.get('category') == 'sex':
			
			if request.form.get('sex') == 'male':
				
				male_survival = [0, 0]
				
				for d in s:
					if d['sex'] == 'male':
						male_survival[1] = male_survival[1] + 1
						if d['survived'] == '1':
							male_survival[0] = male_survival[0] + 1

				result_string = str(male_survival[0]) + ' out of ' + str(male_survival[1]) + ' male passengers survived'
				return render_template("index.html", choice_1 = 'sex', choice_2 = 'm', r_s = result_string)
			
			elif request.form.get('sex') == 'female':

				female_survival = [0, 0]

				for d in s:
					if d['sex'] == 'female':
						female_survival[1] = female_survival[1] + 1
						if d['survived'] == '1':
							female_survival[0] = female_survival[0] + 1
				
				result_string = str(female_survival[0]) + ' out of ' + str(female_survival[1]) + ' female passengers survived'
				return render_template("index.html", choice_1 = 'sex', choice_2 = 'f', r_s = result_string)
			
			else:
				return render_template("index.html", choice_1 = 'sex')

		elif request.form.get('category') == 'class':
			if request.form.get('class') == '1':

				class_1_survival = [0, 0]

				for d in s:
					if d['class'] == '1':
						class_1_survival[1] = class_1_survival[1] + 1
						if d['survived'] == '1':
							class_1_survival[0] = class_1_survival[0] + 1

				result_string = str(class_1_survival[0]) + ' out of ' + str(class_1_survival[1]) + ' passengers in 1st class survived'
				return render_template("index.html", choice_1 = 'class', choice_2 = '1', r_s = result_string)
			
			elif request.form.get('class') == '2':
				
				class_2_survival = [0, 0]

				for d in s:
					if d['class'] == '2':
						class_2_survival[1] = class_2_survival[1] + 1
						if d['survived'] == '1':
							class_2_survival[0] = class_2_survival[0] + 1

				result_string = str(class_2_survival[0]) + ' out of ' + str(class_2_survival[1]) + ' passengers in 2nd class survived'
				return render_template("index.html", choice_1 = 'class', choice_2 = '2', r_s = result_string,)
			
			elif request.form.get('class') == '3':
				
				class_3_survival = [0, 0]

				for d in s:
					if d['class'] == '3':
						class_3_survival[1] = class_3_survival[1] + 1
						if d['survived'] == '1':
							class_3_survival[0] = class_3_survival[0] + 1

				result_string = str(class_3_survival[0]) + ' out of ' + str(class_3_survival[1]) + ' passengers in 3rd class survived'
				return render_template("index.html", choice_1 = 'class', choice_2 = '3', r_s = result_string)
			
			else:
				return render_template("index.html", choice_1 = 'class')

		elif request.form.get('category') == 'age':
			for d in s:
				if [d['age'], 0, 0] not in age_survival:
					age_survival.append([(d)['age'], 0, 0])

			for a in age_survival:
				if a[0] == '':
					age_survival.remove(a)

			for i in age_survival:
				for d in s:
					if d['age'] == i[0]:
						i[2] = i[2] + 1
						if d['survived'] == '1':
							i[1] = i[1] + 1

			if request.form.get('age'):
				for i in age_survival:
					if i[0] == request.form.get('age'):
						result_string = str(i[1]) + ' out of ' + str(i[2]) + ' passengers aged ' + i[0] + ' survived'

						return render_template("index.html", choice_1 = 'age', choice_2 = i[0], r_s = result_string, a_s = sorted(age_survival,key=lambda x: float(x[0])))
			else:
				return render_template("index.html", choice_1 = 'age', a_s = sorted(age_survival,key=lambda x: float(x[0])))



if __name__ == "__main__":
	app.run(debug = True)