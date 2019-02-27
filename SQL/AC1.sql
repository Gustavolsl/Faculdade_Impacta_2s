CREATE TABLE Modelo (
iDModelo INT PRIMARY KEY IDENTITY(1,1),
Descricao VARCHAR(50) 
)

CREATE TABLE Ano (
idAno INT PRIMARY KEY IDENTITY (1 ,1),
Ano VARCHAR(4) NOT NULL
)

CREATE TABLE Mes (
idMes INT PRIMARY KEY IDENTITY(1,1),
mes VARCHAR(2)
)

CREATE TABLE Fabricante (
idFabricante INT PRIMARY KEY IDENTITY(1,1) ,
Nome VARCHAR(50),
Cidade VARCHAR(50),
Endereco VARCHAR(50),
UF VARCHAR(2),
Telefone VARCHAR(11),
Contato VARCHAR(11)
)

CREATE TABLE Veiculo(
idVeiculo INT PRIMARY KEY IDENTITY(1,1),
Descricao VARCHAR(50),
Valor MONEY NOT NULL,
idModelo INT NOT NULL,
idFabricante INT NOT NULL,
idAnoFabricacao INT NOT NULL,
dataCompra VARCHAR(8) NOT NULL,

CONSTRAINT fkidFabricante FOREIGN KEY(idFabricante)
REFERENCES Fabricante(idFabricante),

CONSTRAINT fkidAnoFabricante FOREIGN KEY(idAnoFabricacao)
REFERENCES Ano(idAno)

) 

CREATE TABLE VendasAnuais (
idVendas INT PRIMARY KEY IDENTITY(1,1),
Qtd INT NOT NULL,
idVeiculo INT NOT NULL,
idAnodeVenda INT,
idMesVenda INT

CONSTRAINT fkidVeiculo FOREIGN KEY(idVeiculo)
REFERENCES Veiculo(idVeiculo),

CONSTRAINT fkidAnodeVenda FOREIGN KEY(IDAnodeVenda)
REFERENCES Ano(idAno),

CONSTRAINT fkidMesVenda FOREIGN KEY(idMesVenda)
REFERENCES Mes(idMes)

)