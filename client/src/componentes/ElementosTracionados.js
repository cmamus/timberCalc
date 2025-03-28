import React, { useState } from 'react';
import axios from 'axios';

import "../styles/form.css"

const Tracionados = ({ setControle }) => {

  const [normal, setNormal] = useState('');
  const [mx, setMx] = useState('');
  const [my, setMy] = useState('');
  const [base, setBase] = useState('');
  const [altura, setAltura] = useState('');
  const [area_furos, setArea_furos] = useState('');
  const [comprimento, setComprimento] = useState('');
  const [vinculo_x, setVinculo_x] = useState('');
  const [vinculo_y, setVinculo_y] = useState('');
  const [carregamento, setCarregamento] = useState('');
  const [umidade, setUmidade] = useState('');
  const [ft0k, setFt0k] = useState('');
  const [fmk, setFmk] = useState('');
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

  const handleArea_furosChange = (e) => {
    setArea_furos(e.target.value);
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

  const handleFt0kChange = (e) => {
    setFt0k(e.target.value);
  };

  const handleFmkChange = (e) => {
    setFmk(e.target.value);
  };

  const handleReset = () => {
    setNormal('');
    setMx('');
    setMy('');
    setBase('');
    setAltura('');
    setArea_furos('');
    setComprimento('');
    setVinculo_x('');
    setVinculo_y('');
    setCarregamento('');
    setUmidade('');
    setFt0k('');
    setFmk('');
    setResults({});
  };

  const handleMenu = () => {
    setControle(0);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/tracionados', {
        normal,
        mx,
        my,
        base,
        altura,
        area_furos,
        comprimento,
        vinculo_x,
        vinculo_y,
        carregamento,
        umidade,
        ft0k,
        fmk
      });
      setResults(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="tracionados">
      <div>
        <h1>Elementos Tracionados e Flexotracionados</h1>
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
          <label>Area dos Furos </label>
          <input
            type="number"
            placeholder="Area dos Furos (mm²)"
            value={area_furos}
            onChange={handleArea_furosChange}
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
          <label>Resistência Característica Paralela as Fibras </label>
          <input
            type="number"
            placeholder="ft0k (MPa)"
            value={ft0k}
            onChange={handleFt0kChange}
          />
        </div>
        <div className="input-group">
          <label>Resistência Característica à Flexão </label>
          <input
            type="number"
            placeholder="fmk (Mpa)"
            value={fmk}
            onChange={handleFmkChange}
          />
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
          <p>f<inf>t0,d</inf>: {results.ft0d} MPa</p>
          <p>f<inf>m,d</inf>: {results.fmd} MPa</p>
          <p>A: {results.area} mm<sup>2</sup></p>
          <p>I<inf>x</inf>: {results.inercia_x} mm</p>
          <p>I<inf>y</inf>: {results.inercia_y} mm</p>
          <p>W<inf>x</inf>: {results.mod_res_x} mm<sup>3</sup></p>
          <p>W<inf>y</inf>: {results.mod_res_y} mm<sup>3</sup></p>
          <p>i<inf>x</inf>: {results.raio_gira_x} mm<sup>4</sup></p>
          <p>i<inf>y</inf>: {results.raio_gira_y} mm<sup>4</sup></p>
          <p>λ<inf>x</inf>: {results.lamb_x}</p>
          <p>λ<inf>y</inf>: {results.lamb_y}</p>
          <p>Atende ao Estado Limide de Serviço: {results.passou_els ? 'Sim' : 'Não'}</p>
          <p>σ<inf>N</inf>: {results.sigma_n} MPa</p>
          <p>σ<inf>Mx</inf>: {results.sigma_mx} MPa</p>
          <p>σ<inf>My</inf>: {results.sigma_my} MPa</p>
          <p>ELU 1º Condição: {results.cond_1}</p>
          <p>ELU 2º Condição: {results.cond_2}</p>
          <p>Atende ao Estado Limite Último: {results.passou_elu ? 'Sim' : 'Não'}</p>
        </div>
      )}
    </div>
  );
};

export default Tracionados;