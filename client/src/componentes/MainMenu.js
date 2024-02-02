import React, { useState } from "react";
import Comprimidos from "./ElementosComprimidos";

function MainMenu() {
  const [controle, setControle] = useState(0);
  
  function elementosComprimidos() {
    setControle(1);
  }

  switch (controle) {
    case 0:
      return (
        <div>
          <h1>Main Menu</h1>
          <button onClick={elementosComprimidos}>Elementos Comprimidos e Flexocomprimidos</button>
        </div>
      );
    case 1:
      return (
        <div>
          <Comprimidos setControle={setControle} />          
        </div>
      );
    default:
      return (
        <div>
          <h1>Algo deu errado no controle</h1>
        </div>
      );
  }
}

export default MainMenu;