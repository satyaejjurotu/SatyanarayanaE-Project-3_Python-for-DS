import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'applicantincome':2000, 'coaplicantincome':1000, 'loanamount':400,
                             'loan_amount_term':240,'credit_history':1,'self_employed':1, 
                             'property_area':1, 'married':1, 'education':1, 'gender':1 })

print(r.json())

