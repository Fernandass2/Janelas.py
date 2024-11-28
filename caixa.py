import sys
# importar os componentes para a construção da janela

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap

# Construção da classe janela com o nome de caixa
class Caixa(QWidget):
    
    #criação com o metodo __init__ que inicia a janela e exibe ela em tela
    
    def __init__(self):
        super().__init__()
       
        # Vamos definir a posição e o tamanho da tela
        
        self.setGeometry(0,30,1200,800)

        # Vamos definir o titulo da nossa janela
       
        self.setWindowTitle("Caixa da loja")

        #Vamos criar as labels que representam as colunas, esquerda e direita

        #---------------- Label da esquerda ------------------
        
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#2f6fd6}")

        #---------------- Label da direita ------------------
        
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#8e939c}")

        #------------- Criar o Conteúdo da coluna da esquerda -------------

        self.v_layout_esquerda = QVBoxLayout()

        # Vamos criar uma label para adicionar a logo da nossa loja

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("C:/Users/fernanda.bneris/Documents/Janelas/.venv/resenha.jpg"))

        # Ajudar a label e a imagem para ficar do tamanho ideal

        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedHeight(300)
        self.logo_label.setFixedWidth(350)

        # Adicionar a label com a imagem na tela 

        self.v_layout_esquerda.addWidget(self.logo_label)

        # Vamos criar as labels e as LinesEdits que ficarão  na coluna 
        # esquerda, dentro da layout vertical da esquerda
        
        self.codigo_produto_label = QLabel("Código do Produto: ")
        self.codigo_produto_edit = QLineEdit()
        
        self.codigo_produto_edit = QLineEdit()
        self.codigo_produto_edit.setStyleSheet("QLineEdit{font-size:30px}")

        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codigo_produto_edit)

        self.nome_produto_label = QLabel("Nome do Produto: ")
        self.nome_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.nome_produto_label)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)


        self.descricao_produto_label = QLabel("Descrição do Produto: ")
        self.descricao_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.descricao_produto_label)
        self.v_layout_esquerda.addWidget(self.descricao_produto_edit)

        self.quantidade_produto_label = QLabel("Quantidade do Produto: ")
        self.quantidade_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.quantidade_produto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)

        self.preco_produto_label = QLabel("Preço do Produto: ")
        self.preco_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.preco_produto_label)
        self.v_layout_esquerda.addWidget(self.preco_produto_edit)

        self.preco_unitario_produto_label = QLabel("Preço Unitário do Produto: ")
        self.preco_unitario_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.preco_unitario_produto_label)
        self.v_layout_esquerda.addWidget(self.preco_unitario_produto_edit)

        self.subtotal_produto_label = QLabel("SubTotal do Produto: ")
        self.subtotal_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.subtotal_produto_label)
        self.v_layout_esquerda.addWidget(self.subtotal_produto_edit)

        # Adicionar o layout vertical da esquerda com
        # todos os controles: label e lineEdit dentro da coluna
        # da esqueda(label_coluna_esquerda)

        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)


        #---------------- Controles da Coluna da direita ------------------
        
        self.v_layout_direita = QVBoxLayout()

        
        # Criar uma tabala e adicionar na coluna da direita está tabela terá os nomes 
        # dos campos que estção ao esquerdo. 

        # Colunas da tabela
        colunas = ["Cod. Produto", "Nome do Produto","Descrição","Quantidade","Preço do Produto","Preço Unitário","Subtotal"]
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(25)
        self.v_layout_direita.addWidget(self.tabela)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.total_pagar_label = QLabel("Total a Pagar")
        self.total_pagar_edit = QLineEdit("0,00")
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_pagar_edit) 

        self.label_coluna_direita.setLayout(self.v_layout_direita)


        #Criar o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        #Vamos adicionar as colunas esquerda e direita ao layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        # Adicionar o layout na tela
        self.setLayout(self.h_layout)




app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()
