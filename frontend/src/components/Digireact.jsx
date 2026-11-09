import { useState } from "react";

export default function Digireact() {
    const [digimonList, setDigimonList] = useState([]); // valor inicial array vacío
    // para leer :      digimonList,
    // para escribir :  setDigimonList

    const cargarDigimons = async () => {
        const lista = await fetch("https://digi-api.com/api/v1/digimon");
        const data = await lista.json();
        setDigimonList(data.content); // actualiza el estado con la lista de digimons
    };

    return (
        <div className="my-32 border-t pt-8 pb-32 flex flex-col items-center gap-4">
            <h2 className="text-center text-2xl font-bold">Digireact</h2>
            <div>
                <button type="button" onClick={() => cargarDigimons()} className="rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600">
                    Carga digimons
                </button>
            </div>
            <div className="grid grid-cols-3 gap-4">
                {
                    digimonList.map((digimon) => <div className="border rounded p-4 bg-white shadow" 
                        key={digimon.id}>
                        <div>
                            <h4 className="font-bold">{digimon.name}</h4>
                        </div>
                        <div>
                            <img src={digimon.image} alt={digimon.name} className="w-32 h-32 object-contain" />
                        </div>
                    </div>)
                }
            </div>
        </div>
    );
}