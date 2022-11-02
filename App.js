import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import './App.css';
  
/*
  Nome: Gabriel Gomes
  Idade: 25
  Profissão: Programador
  Email: programador@rethink.dev
  Telefone: (31) 9 9999-9999
  Data de Preenchimento:  19/10/2022

  name
  age
  profisson
  email
  telphone
  date
*/

function App() {
    const [name , setName] = useState('');
    const [age , setAge] = useState('');
    const [profession , setPofession] = useState('');
    const [email , setEmail] = useState('');
    const [telphone , setTelphone] = useState('');
    const hoje = new Date()
    const dia = hoje.getDate().toString().padStart(2,'0')
    const mes = String(hoje.getMonth() + 1).padStart(2,'0')
    const ano = hoje.getFullYear()
    const [date, setDate] = date = `${dia} / ${mes} / ${ano}`;

    // funcao para atualizar o estado do nome
    // com o valor inserido pelo usuario no form
    const handleChange =(e)=>{
      setName(e.target.value);
    }
    // funcao para atualizar o estado da idade
    // com o valor inserido pelo usuario no form
    const handleAgeChange =(e)=>{
      setAge(e.target.value);
    }
    // funcao para atualizar o estado da profissao
    // com o valor inserido pelo usuario no form
    const handleProfessionChange =(e)=>{
        setPofession(e.target.value);
    }
    // funcao para atualizar o estado do email
    // com o valor inserido pelo usuario no form
    const handleEmailChange =(e)=>{
      setEmail(e.target.value);
    }
    // funcao para atualizar o estado do telefone
    // com o valor inserido pelo usuario no form
    const handleTelphoneChange =(e)=>{
        setTelphone(e.target.value);
    }
    // below function will be called when user 
    // click on submit button .
    const handleSubmit=(e)=>{
        // caixa de alerta na tela com 
        // o nome e email do usuario
        alert('Um form foi submetido com nome :"' + name +
        '" ,idade :"'+age +'" e Email :"' + email + '"');
        e.preventDefault();
  
    }
  return (
    <div className="App">
    <header className="App-header">
    <form onSubmit={(e) => {handleSubmit(e)}}>
     {/*when user submit the form , handleSubmit() 
        function will be called .*/}
    <h2> DETRAN </h2>
    <h3> Cadastro </h3>
        <label >
          Name:
        </label><br/>
        <input type="text" value={name} required onChange={(e) => {handleChange(e)}} /><br/>
            {/* quando o usuario escrever na caixa de nome, a funcao handleChange() sera chamada.*/}
        <label >
          Age:
        </label><br/>
        <input type="text" value={age} required onChange={(e) => {handleAgeChange(e)}} /><br/>
            {/* quando o usuario escrever na caixa de idade, a funcao handleAgeChange() sera chamada.*/}
        <label>
          Profession:
        </label><br/>
        <input type="profession" value={profession} required onChange={(e) => {handleProfessionChange(e)}} /><br/>
              {/* quando o usuario escrever na caixa de profissao, a funcao handlePasswordChange() sera chamada.*/}
        <label>
          Email:
        </label><br/>
        <input type="email" value={email} required onChange={(e) => {handleEmailChange(e)}} /><br/>
            {/* quando o usuario escrever na caixa de email, a funcao handleEmailChange() sera chamada.*/}
        <label>
          telphone:
        </label><br/>
        <input type="password" value={telphone} required onChange={(e) => {handleTelphoneChange(e)}} /><br/>
            {/* quando o usuario escrever na caixa de telefone, a funcao handleTelphoneChange() sera chamada.*/}
        <input type="submit" value="Submit"/>
      </form>
    </header>
    </div>
  );
}
  
export default App;