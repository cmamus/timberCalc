import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import MainMenu from "./componentes/MainMenu";
import Comprimido from "./componentes/ElementosComprimidos";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainMenu />} />
        <Route path="/comprimido" element={<Comprimido />} />
      </Routes>
    </Router>
  );
}

export default App;