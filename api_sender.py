from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import requests
from error import InvalidUsage

app = Flask(__name__)
api = Api(app)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
    
@app.route('/create', methods= ['POST'])
def addCurriculo():
    payload = request.get_json()
     
    #The resumè must be sent as a json object, with ALL keys filled with valid values.        
    full_name = list(payload['full_name'])    
    if len(full_name) == 0:
      raise  InvalidUsage('o campo full_name não pode ficar vazio.', status_code=400)
     
    email = list(payload['email'])    
    if len(email) == 0:
      raise  InvalidUsage('o campo email não pode ficar vazio.', status_code=400)

    mobile_phone = list(payload['mobile_phone'])    
    if len(mobile_phone ) == 0:
      raise  InvalidUsage('o campo mobile_phone  não pode ficar vazio.', status_code=400)
    
    age = (payload['age'])  
    if type(age) == int:
       print() 
    else:
       raise InvalidUsage('somente numeros no campo age cidadão') 
   
    home_address = list(payload['home_address'])    
    if len(home_address ) == 0:
      raise  InvalidUsage('o campo home_address não pode ficar vazio.', status_code=400) 
   
    start_date = (payload['start_date']) 
    if type(start_date) == int:
       print() 
    else:
       raise  InvalidUsage('o campo start_date só aceita (Unix epoch) faça a conversão e tente novamente')   
   
    opportunity_tag = list(payload['opportunity_tag'])    
    if len(opportunity_tag ) == 0:
      raise  InvalidUsage('o campo opportunity_tag não pode ficar vazio.', status_code=400)
    
    past_jobs_experience = list(payload['past_jobs_experience'])    
    if len(past_jobs_experience ) == 0:
      raise  InvalidUsage('o campo past_jobs_experience não pode ficar vazio.', status_code=400)
    
    why = list(payload['why'])    
    if len(why) == 0:
      raise  InvalidUsage('o campo why não pode ficar vazio.', status_code=400)
    
    git_url_repositories = list(payload['git_url_repositories'])    
    if len(git_url_repositories) == 0:
      raise  InvalidUsage('o campo git_url_repositories  não pode ficar vazio.', status_code=400)

   
    #Note that *degrees, programming_skills, database_skills* and *hobbies* are arrays.
    degrees = list(payload['degrees'])    
    for i in degrees:
     if not i.get('institution_name'): 
      raise  InvalidUsage('o campo institution_name na aba degrees não pode ficar em branco')
     if not i.get('degree_name'): 
      raise  InvalidUsage('o campo degree_name na aba degrees não pode ficar em branco')
     if type(i.get('begin_date')) == int:
      print() 
     else:
      raise  InvalidUsage('o campo begin_date na aba degrees só aceita (Unix epoch) faça a conversão e tente novamente')  
     if type(i.get('end_date')) == int:
      print() 
     else:
      raise  InvalidUsage('o campo end_date na aba degrees só aceita (Unix epoch) faça a conversão e tente novamente')   

    programming_skills = list(payload['programming_skills'])
    if len(programming_skills) == 0 or  type(programming_skills) != 'list':
      raise  InvalidUsage('o campo programming_skills não pode ficar vazio e somente aceita arrays.', status_code=400)

    database_skills = list(payload['database_skills'])
    if len(database_skills) == 0 or  type(database_skills) != 'list':
      raise  InvalidUsage('o campo database_skills não pode ficar vazio e somente aceita arrays.', status_code=400)

    hobbies = list(payload['hobbies'])
    if len(hobbies) == 0 or  type(hobbies) != 'list':
      raise  InvalidUsage('o campo hobbies não pode ficar vazio e somente aceita arrays.', status_code=400)

  
    #chama api post_resume
    retorno_api = requests.post('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume',data =None, json=  payload)
    if retorno_api.status_code == 200:
        return retorno_api.json()
    if retorno_api.status_code == 500:
        raise  InvalidUsage('Dados não podem ser vazios', status_code=400)


if __name__ == '__main__':
    app.run(debug=True, port=8080)