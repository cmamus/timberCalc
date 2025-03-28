import math
from flask import Flask, request, jsonify
from flask_cors import CORS

pi = math.pi

app = Flask(__name__)

CORS(app)

################################################ Classes da Madeira #################################################
nativa = [
            ['Nativa D20', 20, 4, 10000, 500],
            ['Nativa D30', 30, 5, 12000, 625],
            ['Nativa D40', 40, 6, 14500, 750],
            ['Nativa D50', 50, 7, 16500, 850],
            ['Nativa D60', 60, 8, 19500, 1000]
             ]

coniferas = [
            ['Conífera C14', 14, 8,  0.4, 16, 2.0, 3.0, 7000, 4700, 200, 400, 290],
            ['Conífera C16', 16, 10, 0.4, 17, 2.2, 3.2, 8000, 5400, 300, 500, 310],
            ['Conífera C18', 18, 11, 0.4, 18, 2.2, 3.4, 9000, 6000, 300, 600, 320],
            ['Conífera C20', 20, 12, 0.4, 19, 2.3, 3.6, 9500, 6400, 300, 600, 330],
            ['Conífera C22', 22, 13, 0.4, 20, 2.4, 3.8, 10000, 6700, 300, 600, 340],
            ['Conífera C24', 24, 14, 0.4, 21, 2.5, 4.0, 11000, 7400, 400, 700, 350],
            ['Conífera C27', 27, 16, 0.4, 22, 2.6, 4.0, 12000, 7700, 400, 700, 370],
            ['Conífera C30', 30, 18, 0.4, 23, 2.7, 4.0, 12000, 8000, 400, 800, 380],
            ['Conífera C35', 35, 21, 0.4, 25, 2.8, 4.0, 13000, 8700, 400, 800, 400],
            ['Conífera C40', 40, 24, 0.4, 26, 2.9, 4.0, 14000, 9400, 500, 900, 420],
            ['Conífera C45', 45, 27, 0.4, 27, 3.1, 4.0, 15000, 10000, 500, 900, 440],
            ['Conífera C50', 50, 30, 0.4, 29, 3.2, 4.0, 16000, 11000, 500, 1000, 460]
             ]

folhosas = [
            ['Folhosa D18', 18, 11, 0.6, 18, 7.5, 3.4, 9500, 8000, 600, 600, 475, 570],
            ['Folhosa D24', 24, 14, 0.6, 21, 7.8, 4.0, 10000, 8500, 700, 600, 485, 580],
            ['Folhosa D30', 30, 18, 0.6, 23, 8.0, 4.0, 11000, 9200, 700, 700, 530, 640],
            ['Folhosa D35', 35, 21, 0.6, 25, 8.1, 4.0, 12000, 10000, 800, 800, 540, 650],
            ['Folhosa D40', 40, 24, 0.6, 26, 8.3, 4.0, 13000, 11000, 900, 800, 560, 660],
            ['Folhosa D50', 50, 30, 0.6, 29, 9.3, 4.0, 14000, 12000, 900, 900, 620, 750],
            ['Folhosa D60', 60, 36, 0.6, 32, 11.0, 4.5, 17000, 14000, 1100, 1100, 700, 840],
            ['Folhosa D70', 70, 42, 0.6, 34, 13.0, 5.0, 20000, 16800, 1330, 1250, 900, 1080]
             ]

############################## Formulario 3 - Elementos Tracionados e Flexotracionados ##############################

@app.route('/tracionados', methods=['POST'])
def tracionados():
    
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
    carregamento = kmod1.get(data.get("carregamento"))
    
    kmod2 = {
        "classe1": 1,
        "classe2": 0.9,
        "classe3": 0.8,
        "classe4": 0.7,
        "submersa": 0.65,
    }
    umidade = kmod2.get(data.get("umidade"))
      
    #Passo 2: Propriedades do Material
    ft = {
        "Nativa D20": 20,
        "Nativa D30": 30,
        "Nativa D40": 40,
        "Nativa D50": 50,
        "Nativa D60": 60,
        "Conífera C14": 8,
        "Conífera C16": 10,
        "Conífera C18": 11,
        "Conífera C20": 12,
        "Conífera C22": 13,
        "Conífera C24": 14,
        "Conífera C27": 16,
        "Conífera C30": 18,
        "Conífera C35": 21,
        "Conífera C40": 24,
        "Conífera C45": 27,
        "Conífera C50": 30,
        "Folhosa D18": 11,
        "Folhosa D24": 14,
        "Folhosa D30": 18,
        "Folhosa D35": 21,
        "Folhosa D40": 24,
        "Folhosa D50": 30,
        "Folhosa D60": 36,
        "Folhosa D70": 42,
    }
    madeira = ft.get(data.get("ft0k"))

    fm = {
        "Nativa D20": 20,
        "Nativa D30": 30,
        "Nativa D40": 40,
        "Nativa D50": 50,
        "Nativa D60": 60,
        "Conífera C14": 14,
        "Conífera C16": 16,
        "Conífera C18": 18,
        "Conífera C20": 20,
        "Conífera C22": 22,
        "Conífera C24": 24,
        "Conífera C27": 27,
        "Conífera C30": 30,
        "Conífera C35": 35,
        "Conífera C40": 40,
        "Conífera C45": 45,
        "Conífera C50": 50,
        "Folhosa D18": 18,
        "Folhosa D24": 24,
        "Folhosa D30": 30,
        "Folhosa D35": 35,
        "Folhosa D40": 40,
        "Folhosa D50": 50,
        "Folhosa D60": 60,
        "Folhosa D70": 70,
    }
    madeira = fm.get(data.get("fmk"))
    
    madeira = data.get("madeira", "").strip()

    ft0k = ft.get(madeira)
    fmk = fm.get(madeira)

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

    print(f"sigma_n: {sigma_n}, sigma_mx: {sigma_mx}, sigma_my: {sigma_my}, ft0d: {ft0d}, fmd: {fmd}, kmod1: {carregamento}, kmod2: {umidade}")

    cond_1 = (sigma_n / ft0d) + (sigma_mx / fmd) + (0.7 * sigma_my / fmd)
    cond_2 = (sigma_n / ft0d) + (0.7 * sigma_mx / fmd) + (sigma_my / fmd)

    passou_elu = cond_1 <= 1 and cond_2 <=1

    results = {
        'madeira' : madeira,
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

############################## Formulario 4 - Elementos Comprimidos e Flexocomprimidos ##############################

@app.route('/comprimidos', methods=['POST'])
def comprimidos():
    
    #Passo 1: Esforcos
    data = request.get_json()
    print(data)
    
    normal = float(data['normal'])
    mx = float(data['mx'])
    my = float(data['my'])
    
    base = float(data['base'])
    altura = float(data['altura'])
        
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
        "classe2": 0.9,
        "classe3": 0.8,
        "classe4": 0.7,
        "submersa": 0.65,
    }
    umidade = kmod2.get(data.get("umidade"), 1)

    tipo_madeira = {
        "serrada": 0.2,
        "engenheirada": 0.1,
    }
    beta_c = tipo_madeira.get(data.get("beta_c"), 0.2)
      
    #Passo 2: Propriedades do Material
    fc = {
        "Nativa D20": 20,
        "Nativa D30": 30,
        "Nativa D40": 40,
        "Nativa D50": 50,
        "Nativa D60": 60,
        "Conífera C14": 16,
        "Conífera C16": 17,
        "Conífera C18": 18,
        "Conífera C20": 19,
        "Conífera C22": 20,
        "Conífera C24": 21,
        "Conífera C27": 22,
        "Conífera C30": 23,
        "Conífera C35": 25,
        "Conífera C40": 26,
        "Conífera C45": 27,
        "Conífera C50": 29,
        "Folhosa D18": 18,
        "Folhosa D24": 21,
        "Folhosa D30": 23,
        "Folhosa D35": 25,
        "Folhosa D40": 26,
        "Folhosa D50": 29,
        "Folhosa D60": 32,
        "Folhosa D70": 34,
    }
    madeira = fc.get(data.get("fc0k"))

    fm = {
        "Nativa D20": 20,
        "Nativa D30": 30,
        "Nativa D40": 40,
        "Nativa D50": 50,
        "Nativa D60": 60,
        "Conífera C14": 14,
        "Conífera C16": 16,
        "Conífera C18": 18,
        "Conífera C20": 20,
        "Conífera C22": 22,
        "Conífera C24": 24,
        "Conífera C27": 27,
        "Conífera C30": 30,
        "Conífera C35": 35,
        "Conífera C40": 40,
        "Conífera C45": 45,
        "Conífera C50": 50,
        "Folhosa D18": 18,
        "Folhosa D24": 24,
        "Folhosa D30": 30,
        "Folhosa D35": 35,
        "Folhosa D40": 40,
        "Folhosa D50": 50,
        "Folhosa D60": 60,
        "Folhosa D70": 70,
    }
    madeira = fm.get(data.get("fmk"))

    e = {
        "Nativa D20": 7000,
        "Nativa D30": 8400,
        "Nativa D40": 10150,
        "Nativa D50": 11550,
        "Nativa D60": 13650,
        "Conífera C14": 4700,
        "Conífera C16": 5400,
        "Conífera C18": 6000,
        "Conífera C20": 6400,
        "Conífera C22": 6700,
        "Conífera C24": 7400,
        "Conífera C27": 7700,
        "Conífera C30": 8000,
        "Conífera C35": 8700,
        "Conífera C40": 9400,
        "Conífera C45": 10000,
        "Conífera C50": 11000,
        "Folhosa D18": 8000,
        "Folhosa D24": 8500,
        "Folhosa D30": 9200,
        "Folhosa D35": 10000,
        "Folhosa D40": 11000,
        "Folhosa D50": 12000,
        "Folhosa D60": 14000,
        "Folhosa D70": 16800,
    }
    madeira = e.get(data.get("e005"))
    
    madeira = data.get("madeira", "").strip()

    fc0k = fc.get(madeira)
    fmk = fm.get(madeira)
    e005 = e.get(madeira)

    fc0d = fc0k * carregamento * umidade / 1.4
    fmd = fmk * carregamento * umidade / 1.4
    
    #Passo 3: Propriedades Geometricas
    area = base * altura
    
    inercia_x = (base * altura ** 3) / 12
    inercia_y = (altura * base ** 3) / 12
    
    mod_res_x = (base * altura ** 2) / 6
    mod_res_y = (altura * base ** 2) / 6
    
    raio_gira_x = math.sqrt(inercia_x / area)
    raio_gira_y = math.sqrt(inercia_y / area)

    lamb_x = comprimento * vinculo_x / raio_gira_x
    lamb_y = comprimento * vinculo_y / raio_gira_y

    lamb_rel_x = (lamb_x / pi) * (math.sqrt(fc0k / e005))
    lamb_rel_y = (lamb_y / pi) * (math.sqrt(fc0k / e005))

    #Passo 4: ELS
    passou_els = lamb_x < 140 and lamb_y < 140
    
    #Passo 5: ELU Centrado
    if mx == 0 and my == 0:
        
        sigma_n = normal / area

        if lamb_rel_x > 0.3 and lamb_rel_y > 0.3:

            kx = 0.5 * (1 + (beta_c * (lamb_rel_x - 0.3) + (lamb_rel_x ** 2)))
            ky = 0.5 * (1 + (beta_c * (lamb_rel_y - 0.3) + (lamb_rel_y ** 2)))

            kcx = 1 / (kx + (math.sqrt((kx ** 2) - (lamb_rel_x **2))))
            kcy = 1 / (ky + (math.sqrt((ky ** 2) - (lamb_rel_y **2))))

            cond_1 = sigma_n / (fc0d * kcx)
            cond_2 = sigma_n / (fc0d * kcy)
 
            passou_elu = cond_1 <= 1 and cond_2 <=1

            results = {
                'madeira' : madeira,
                'fc0d' : round(fc0d, 2),
                'fmd' : round(fmd, 2),
                'e005' : e005,
                'area' : round(area, 2),
                'inercia_x' : round(inercia_x, 3),
                'inercia_y' : round(inercia_y, 3),
                'mod_res_x' : round(mod_res_x, 3),
                'mod_res_y' : round(mod_res_y, 3),
                'raio_gira_x' : round(raio_gira_x, 3),
                'raio_gira_y' : round(raio_gira_y, 3),
                'lamb_x' : round(lamb_x, 3),
                'lamb_y' : round(lamb_y, 3),
                'lamb_rel_x' : round(lamb_x, 3),
                'lamb_rel_y' : round(lamb_y, 3),
                'passou_els' : passou_els,
                'sigma_n' : round(sigma_n, 2),
                'cond_1' : round(cond_1, 4),
                'cond_2' : round(cond_2, 4),
                'passou_elu' : passou_elu,
            }

        else:

            cond_1 = sigma_n / fc0d

            cond_2 = "Não se aplica!"

            passou_elu = cond_1 <= 1

            results = {
                'madeira' : madeira,
                'fc0d' : round(fc0d, 2),
                'fmd' : round(fmd, 2),
                'e005' : e005,
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
                'cond_1' : round(cond_1, 4),
                'cond_2' : cond_2,
                'passou_elu' : passou_elu,
            }

    #Passo 6: ELU Excentrico
    else:

        sigma_n = normal / area
        sigma_mx = mx / mod_res_x
        sigma_my = my / mod_res_y

        if  lamb_rel_x > 0.3 and lamb_rel_y > 0.3:

            kx = 0.5 * (1 + (beta_c * (lamb_rel_x - 0.3) + (lamb_rel_x ** 2)))
            ky = 0.5 * (1 + (beta_c * (lamb_rel_y - 0.3) + (lamb_rel_y ** 2)))

            kcx = 1 / (kx + (math.sqrt((kx ** 2) - (lamb_rel_x **2))))
            kcy = 1 / (ky + (math.sqrt((ky ** 2) - (lamb_rel_y **2))))

            cond_1 = (sigma_n / (fc0d * kcx)) + (sigma_mx / fmd) + (0.7 * (sigma_my / fmd))
            cond_2 = (sigma_n / (fc0d * kcy)) + (0.7 * (sigma_mx / fmd)) + (sigma_my / fmd)

            passou_elu = cond_1 <= 1 and cond_2 <=1


            results = {
                'madeira' : madeira,
                'fc0d' : round(fc0d, 2),
                'fmd' : round(fmd, 2),
                'e005' : e005,
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

        else:

            cond_1 = ((sigma_n / fc0d) ** 2) + (sigma_mx / fmd) + (0.7 * (sigma_my / fmd))
            cond_2 = ((sigma_n / fc0d) ** 2) + (0.7 * (sigma_mx / fmd)) + (sigma_my / fmd)

            passou_elu = cond_1 <= 1 and cond_2 <=1

            results = {
                'madeira' : madeira,
                'fc0d' : round(fc0d, 2),
                'fmd' : round(fmd, 2),
                'e005' : e005,
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

'''
@app.route('/fletidos', methods=['POST'])
def fletidos():
    
    #Passo 1: Esforcos
    data = request.get_json()
    print(data)
    
    normal = float(data['normal'])
    mx = float(data['mx'])
    my = float(data['my'])
    vd = float(data['vd'])
    
    base = float(data['base'])
    altura = float(data['altura'])
        
    comprimento = float(data['comprimento'])
    
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
    e0ef = float(data['e0ef'])
    beta_m = float(data['beta_m'])
    fmk = float(data['fmk'])
    ft0k = float(data['ft0k'])
    fc0k = float(data['fc0k'])
    fvk = float(data['fvk'])
    fc90k = float(data['fc90k'])
    
    fmd = fmk * carregamento * umidade / 1.4
    ft0d = ft0k * carregamento * umidade / 1.4
    fc0d = fc0k * carregamento * umidade / 1.4
    fvd = fvk * carregamento * umidade / 1.8
    fc90d = fc90k * carregamento * umidade / 1.4

    a_esmagamento = float(data['a_esmagamento'])
    
    #Passo 3: Propriedades Geometricas
    area = base * altura
    
    inercia_x = (base * altura ** 3) / 12
    inercia_y = (altura * base ** 3) / 12
    
    mod_res_x = (base * altura ** 2) / 6
    mod_res_y = (altura * base ** 2) / 6
    
    #Passo 4: ELS (Flecha)


    #Passo 5: ELU (Estabilidade Lateral)


    #Passo 6: ELU (Tensões Normais)


    #Passo 7: ELU (Tensões Tangenciais)


    #Passo 8: ELU (Esmagamento do Apoio)
'''

if __name__ == '__main__':
    app.run(debug=True)