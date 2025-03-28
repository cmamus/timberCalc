import React, { useState } from 'react';
import axios from 'axios';

import "../styles/form.css"

const Comprimidos = ({ setControle }) => {

  const [normal, setNormal] = useState('');
  const [mx, setMx] = useState('');
  const [my, setMy] = useState('');
  const [base, setBase] = useState('');
  const [altura, setAltura] = useState('');
  const [comprimento, setComprimento] = useState('');
  const [vinculo_x, setVinculo_x] = useState('');
  const [vinculo_y, setVinculo_y] = useState('');
  const [carregamento, setCarregamento] = useState('');
  const [umidade, setUmidade] = useState('');
  const [beta_c, setBeta_c] = useState('');
  const [madeira, setMadeira] = useState('');
  const [results, setResults] = useState({});

  const handleNormalChange = (e) => {
    setNormal(e.target.value);
  };

  const handleMxChange = (e) => {
    setMx(e.target.value);
  };

  const handleMyChange = (e) => {
    setMy(e.target.value);
  };

  const handleBaseChange = (e) => {
    setBase(e.target.value);
  };

  const handleAlturaChange = (e) => {
    setAltura(e.target.value);
  };

  const handleComprimentoChange = (e) => {
    setComprimento(e.target.value);
  };

  const handleVinculo_xChange = (e) => {
    setVinculo_x(e.target.value);
  };

  const handleVinculo_yChange = (e) => {
    setVinculo_y(e.target.value);
  };

  const handleCarregamentoChange = (e) => {
    setCarregamento(e.target.value);
  };

  const handleUmidadeChange = (e) => {
    setUmidade(e.target.value);
  };

  const handleBeta_cChange = (e) => {
    setBeta_c(e.target.value);
  };

  const handleMadeiraChange = (e) => {
    setMadeira(e.target.value);
  };

  const handleReset = () => {
    setNormal('');
    setMx('');
    setMy('');
    setBase('');
    setAltura('');
    setComprimento('');
    setVinculo_x('');
    setVinculo_y('');
    setCarregamento('');
    setUmidade('');
    setBeta_c('');
    setMadeira('');
    setResults({});
  };

  const handleMenu = () => {
    setControle(0);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/comprimidos', {
        normal,
        mx,
        my,
        base,
        altura,
        comprimento,
        vinculo_x,
        vinculo_y,
        carregamento,
        umidade,
        beta_c,
        madeira
      });
      setResults(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="Comprimidos">
      <div>
        <h1>Elementos Comprimidos e Flexotracomprimidos</h1>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>Normal </label>
          <input
            type="number"
            placeholder="Normal (N)"
            value={normal}
            onChange={handleNormalChange}
          />
        </div>
        <div className="input-group">
          <label>Momento em X </label>
          <input
            type="number"
            placeholder="Mx (N.mm)"
            value={mx}
            onChange={handleMxChange}
          />
        </div>
        <div className="input-group">
          <label>Momento em Y </label>
          <input
            type="number"
            placeholder="My (N.mm)"
            value={my}
            onChange={handleMyChange}
          />
        </div>
        <div className="input-group">
          <label>Base </label>
          <input
            type="number"
            placeholder="Base (mm)"
            value={base}
            onChange={handleBaseChange}
          />
        </div>
        <div className="input-group">
          <label>Altura </label>
          <input
            type="number"
            placeholder="Altura (mm)"
            value={altura}
            onChange={handleAlturaChange}
          />
        </div>
        <div className="input-group">
          <label>Comprimento </label>
          <input
            type="number"
            placeholder="Comprimento (mm)"
            value={comprimento}
            onChange={handleComprimentoChange}
          />
        </div>
        <div className="input-group">
          <label htmlFor="options">Vinculo em X: </label>
          <select id="options" value={vinculo_x} onChange={handleVinculo_xChange}>
            <option value="">Selecione uma opção</option>
            <option value="engaste-engaste">Engaste - Engaste</option>
            <option value="engaste-apoio">Engaste - Apoio</option>
            <option value="apoio-apoio">Apoio - Apoio</option>
            <option value="engaste-engastemovel">Engaste - Engaste Móvel</option>
            <option value="engaste-livre">Engaste - Livre</option>
            <option value="apoio-engastemovel">Apoio - Engaste Móvel</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="options">Vinculo em Y: </label>
          <select id="options" value={vinculo_y} onChange={handleVinculo_yChange}>
            <option value="">Selecione uma opção</option>
            <option value="engaste-engaste">Engaste - Engaste</option>
            <option value="engaste-apoio">Engaste - Apoio</option>
            <option value="apoio-apoio">Apoio - Apoio</option>
            <option value="engaste-engastemovel">Engaste - Engaste Móvel</option>
            <option value="engaste-livre">Engaste - Livre</option>
            <option value="apoio-engastemovel">Apoio - Engaste Móvel</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="options">Classe de Carregamento (kmod1): </label>
          <select id="options" value={carregamento} onChange={handleCarregamentoChange}>
            <option value="">Selecione uma opção</option>
            <option value="permanente">Permanete</option>
            <option value="longa">Longa Duração</option>
            <option value="media">Média Duração</option>
            <option value="curta">Curta Duração</option>
            <option value="instantanea">Instantânea</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="options">Classe de Umidade (kmod2): </label>
          <select id="options" value={umidade} onChange={handleUmidadeChange}>
            <option value="">Selecione uma opção</option>
            <option value="classe1">Classe 1</option>
            <option value="classe2">Classe 2</option>
            <option value="classe3">Classe 3</option>
            <option value="classe4">Classe 4</option>
            <option value="submersa">Madeira Submersa</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="options">Classe da Madeira </label>
          <select id="options" value={madeira} onChange={handleMadeiraChange}>
            <option value="">Selecione uma opção</option>
            <option value="Nativa D20">Nativa D20</option>
            <option value="Nativa D30">Nativa D30</option>
            <option value="Nativa D40">Nativa D40</option>
            <option value="Nativa D50">Nativa D50</option>
            <option value="Nativa D60">Nativa D60</option>
            <option value="Conífera C14">Conífera C14</option>
            <option value="Conífera C16">Conífera C16</option>
            <option value="Conífera C18">Conífera C18</option>
            <option value="Conífera C20">Conífera C20</option>
            <option value="Conífera C22">Conífera C22</option>
            <option value="Conífera C24">Conífera C24</option>
            <option value="Conífera C27">Conífera C27</option>
            <option value="Conífera C30">Conífera C30</option>
            <option value="Conífera C35">Conífera C35</option>
            <option value="Conífera C40">Conífera C40</option>
            <option value="Conífera C45">Conífera C45</option>
            <option value="Conífera C50">Conífera C50</option>
            <option value="Folhosa D18">Folhosa D18</option>
            <option value="Folhosa D24">Folhosa D24</option>
            <option value="Folhosa D30">Folhosa D30</option>
            <option value="Folhosa D35">Folhosa D35</option>
            <option value="Folhosa D40">Folhosa D40</option>
            <option value="Folhosa D50">Folhosa D50</option>
            <option value="Folhosa D60">Folhosa D40</option>
            <option value="Folhosa D70">Folhosa D50</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="options">Tipo de Madeira: </label>
          <select id="options" value={beta_c} onChange={handleBeta_cChange}>
            <option value="">Selecione uma opção</option>
            <option value="serrada">Madeira Serrada e Peças Roliças</option>
            <option value="engenheirada">MLC, LVL ou CLT</option>
          </select>
        </div>       
        <button type="submit">
          Calcular
        </button>
        <button type="button" onClick={handleReset}>
          Novo
        </button>
      </form>
      <div>
        <button type="button" onClick={handleMenu}>
          Menu
        </button>
      </div>
      {Object.keys(results).length > 0 && (
        <div>
          <h3>Resultados:</h3>
          <p>f<sub>c0,d</sub>: {results.fc0d} MPa</p>
          <p>f<sub>m,d</sub>: {results.fmd} MPa</p>
          <p>A: {results.area} mm<sup>2</sup></p>
          <p>I<sub>x</sub>: {results.inercia_x} mm<sup>4</sup></p>
          <p>I<sub>y</sub>: {results.inercia_y} mm<sup>4</sup></p>
          <p>W<sub>x</sub>: {results.mod_res_x} mm<sup>3</sup></p>
          <p>W<sub>y</sub>: {results.mod_res_y} mm<sup>3</sup></p>
          <p>i<sub>x</sub>: {results.raio_gira_x} mm</p>
          <p>i<sub>y</sub>: {results.raio_gira_y} mm</p>
          <p>λ<sub>x</sub>: {results.lamb_x}</p>
          <p>λ<sub>y</sub>: {results.lamb_y}</p>
          <p>λ<sub>rel,x</sub>: {results.lamb_rel_x}</p>
          <p>λ<sub>rel,y</sub>: {results.lamb_rel_y}</p>
          <p>Atende ao Estado Limide de Serviço: {results.passou_els ? 'Sim' : 'Não'}</p>
          <p>σ<sub>N</sub>: {results.sigma_n} MPa</p>
          <p>σ<sub>Mx</sub>: {results.sigma_mx} MPa</p>
          <p>σ<sub>My</sub>: {results.sigma_my} MPa</p>
          <p>ELU 1º Condição: {results.cond_1}</p>
          <p>ELU 2º Condição: {results.cond_2}</p>
          <p>Atende ao Estado Limite Último: {results.passou_elu ? 'Sim' : 'Não'}</p>
        </div>
      )}
    </div>
  );
};

export default Comprimidos;