import tkinter as tk;
from tkinter import messagebox;
import json;
import requests;

class App(tk.Frame):
    """receive info about the user CEP and display it in the screen with tkinter.""";

    def __init__(self, master, username):
        #defindo a janela pai
        super().__init__(master);
        #ajustando o objeto inteiro
        self.pack();
        #nome do usuário
        self.username = username;

        #dando oi
        tk.Label(self,text=f"Hello {self.username}, this app is made for get information about your CEP id.").pack(pady=35);

        #separando uma divisão para os widgets dessa classe
        self.info_frame = tk.Frame().pack();

        tk.Label(self.info_frame,text="Type your CEP id:").pack();
        #definindo input

        #cria a variavel que vai ser usada para o tkinter.Entry() do cep
        self.cep_entry_value = tk.StringVar();
        
        #metodo pack() retorna None, por isso terei que criar uma var com somente o objeto tkinter.Entry()..
        self.cep_entry = tk.Entry(self.info_frame, textvariable=self.cep_entry_value);

        #entry renderizado no app
        self.cep_entry.pack();
        #botão que envia o informação do entry para o metodo request
        self.cep_entry_button = tk.Button(self.info_frame, text="Enviar", command=self.get_cep_data);
        self.cep_entry_button.pack(pady=20);
        
        # Associa o evento "Return" (Enter pressionado) à função on_enter_pressed
        self.cep_entry.bind("<Key-Return>", self.get_cep_data);

    ##
    # CLASSES:
    # Quando você chama um método em uma instância da classe,
    # o Python automaticamente passa a própria instância como o primeiro argumento (nomeado por convenção como self) para o método.
    # Isso permite que você acesse todos os atributos e métodos da instância dentro do método.
    ##
    
    ##
    # funçaõ que pega o cep e retorn as informacoes sobvre ele com um request para apicep
    # Quando o evento "Return" ocorre, o Tkinter passará automaticamente um objeto de evento para a função get_cep_data. 
    # No entanto, quando a função é chamada diretamente pelo botão (através do parâmetro command), nenhum objeto de evento é passado.
    ##
    def get_cep_data(self, event=None):
        cep_data = self.cep_entry_value.get();
        
        #conteudo com resposta do endereço digitado
        r = requests.get(f'https://viacep.com.br/ws/{cep_data}/json/');
        
        #tomada de ações a partir do status do response..
        match r.status_code:
            
            #caso a resposta for negativa, como um erro..
            case 401 | 400 | 404 | 503:
                messagebox.showerror("unavailble_cep", "Type a correct CEP.");
                
            #caso de certo..
            case 200:
                content = r.text;
                
                #se endereço não for encontrado:
                if 'erro' in content:#se houver DENTRO DA LIST (in) uma chave erro..
                    messagebox.showwarning('not_found', f' The ID CEP {cep_data} was not not found.');
                else:
                    #recuperando o conteudo em texto e retornando ele na tela formatada
                    self.render_address_content(self.info_frame, content);
            
            #como patrão, o código só continua
            case _:
                pass;

    def render_address_content(self, frame, payload):
        
        #resetando a função..
        txt.pack_forget();
        address.pack_forget();
        province.pack_forget();
        local.pack_forget();
        uf.pack_forget();
        
        list_data = json.loads(payload);
        ##
        # {'cep': '08240-075', 'logradouro': 'Rua Roque Polidoro', 'complemento': '', 'bairro': 'Jardim Liderança', 'localidade': 'São Paulo', 'uf': 'SP', 'ibge': '3550308', 'gia': '1004', 'ddd': '11', 'siafi': '7107'}
        # ##
        
        #ajustando os elementos..
        txt = tk.Label(frame, text=f"Your address information:\n");
        address = tk.Label(frame, text=f"Logradouro:{list_data['logradouro']}\n");
        province = tk.Label(frame, text=f"Bairro:{list_data['bairro']}\n");
        local = tk.Label(frame, text=f"Cidade:{list_data['localidade']}\n");
        uf = tk.Label(frame, text=f"UF:{list_data['uf']}\n");

        #renderizando os elelkmentos..
        txt.pack(pady=1);
        address.pack(pady=1);
        province.pack(pady=1);
        local.pack(pady=1);
        uf.pack(pady=1);
