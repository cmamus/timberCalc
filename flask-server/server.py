import math
from flask import Flask, request, jsonify

app = Flask(__name__)

#Formulário 3
@app.route('/calculate', methods=['POST'])
def calculate():
    
    #Passo 1: Esforços
    data = request.get_json()
    print(data)
    
    normal = float(data['normal'])
    mx = float(data['mx'])
    my = float(data['my'])
    
    base = float(data['base'])
    altura = float(data['altura'])
    
    area_furos = float(data['area_furos'])
    
    comprimento = float(data['comprimento'])
    
    vx = {
        "engaste-engaste": 0.65,
        "engaste-apoio": 0.8,
        "apoio-apoio": 1,
        "engaste-engastemovel": 1.2,
        "engaste-livre": 2,
        "apoio-engastemovel": 2.4,
    }
    vinculo_x = vx.get(data.get("vinculo_x"), 1)
    
    vy = {
        "engaste-engaste": 0.65,
        "engaste-apoio": 0.8,
        "apoio-apoio": 1,
        "engaste-engastemovel": 1.2,
        "engaste-livre": 2,
        "apoio-engastemovel" : 2.4,
    }
    vinculo_y = vy.get(data.get("vinculo_y"), 1)
    
    kmod1 = {
        "permanente": 0.6,
        "longa": 0.7,
        "media": 0.8,
        "curta": 0.9,
        "instantanea": 1.1,
    }
    carregamento = kmod1.get(data.get("carregamento"), 0.6)
    
    kmod2 = {
        "classe1": 1,
        "classe2": 0.95,
        "classe3": 0.93,
        "classe4": 0.9,
        "submersa": 0.65,
    }
    umidade = kmod2.get(data.get("umidade"), 1)
      
    #Passo 2: Propriedades do Material
    ft0k = float(data['ft0k'])
    fmk = float(data['fmk'])

    ft0d = ft0k * carregamento * umidade / 1.4
    fmd = fmk * carregamento * umidade / 1.4
    
    #Passo 3: Propriedades Geométricas
    area = base * altura
    
    inercia_x = (base * altura ** 3) / 12
    inercia_y = (altura * base ** 3) / 12
    
    mod_res_x = (base * altura ** 2) / 6
    mod_res_y = (altura * base ** 2) / 6
    
    raio_gira_x = math.sqrt(inercia_x / area)
    raio_gira_y = math.sqrt(inercia_y / area)

    #Passo 4: Esbeltez
    lamb_x = comprimento * vinculo_x / raio_gira_x
    lamb_y = comprimento * vinculo_y / raio_gira_y

    #Passo 5: ELS
    passou_els = lamb_x < 173 and lamb_y < 173
    
    #Passo 6: ELU
    sigma_n = normal / (area - area_furos)
    sigma_mx = mx / (area - area_furos)
    sigma_my = my / (area - area_furos)

    cond_1 = (sigma_n / ft0d) + (sigma_mx / fmd) + (0.7 * sigma_my / fmd)
    cond_2 = (sigma_n / ft0d) + (0.7 * sigma_mx / fmd) + (sigma_my / fmd)

    passou_elu = cond_1 <= 1 and cond_2 <=1

    results = {
        'ft0d' : round(ft0d, 2),
        'fmd' : round(fmd, 2),
        'area' : round(area, 2),
        'inercia_x' : round(inercia_x, 3),
        'inercia_y' : round(inercia_y, 3),
        'mod_res_x' : round(mod_res_x, 3),
        'mod_res_y' : round(mod_res_y, 3),
        'raio_gira_x' : round(raio_gira_x, 3),
        'raio_gira_y' : round(raio_gira_y, 3),
        'lamb_x' : round(lamb_x, 3),
        'lamb_y' : round(lamb_y, 3),
        'passou_els' : passou_els,
        'sigma_n' : round(sigma_n, 2),
        'sigma_mx' : round(sigma_mx, 2),
        'sigma_my' : round(sigma_my, 2),
        'cond_1' : round(cond_1, 4),
        'cond_2' : round(cond_2, 4),
        'passou_elu' : passou_elu,
    }

    print(results)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)