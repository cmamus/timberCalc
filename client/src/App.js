import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import MainMenu from "./componentes/MainMenu";
import Comprimidos from "./componentes/ElementosComprimidos";
import Tracionados from "./componentes/ElementosTracionados";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainMenu />} />
        <Route path="/comprimido" element={<Comprimidos />} />
        <Route path="/tracionado" element={<Tracionados />} />
      </Routes>
    </Router>
  );
}

export default App;