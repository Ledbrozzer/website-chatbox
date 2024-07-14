#terminal -> " + " -> Prompt command ->
#   pip install flet
# pip install flet 
#ctrl + c (on the terminal to stop)
import flet as ft
#flet python documentatio and tools
def main(pagina):
    titulo = ft.Text("ImpactTrainer")
    #socket => tunnel de comunicação
    # pagina.bgcolor=""
    
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        #print(mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)#create the tunnel
    #pagina.pubsub.send_all()

    titulo_janela = ft.Text("Bem-Vindo")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    
    def enviar_mensagem (evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        #  chat.controls.append(ft.Text(texto))

        pagina.pubsub.send_all(texto)
        texto_mensagem.value = ""
        pagina.update()
        # arquivo = ft.FilePicker()
    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    

    chat = ft.Column()
    
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        # pagina.update()
        # pagina.add(texto_mensagem)
        # pagina.add(botao_enviar)
        pagina.add(chat)
        pagina.add(linha_mensagem)


        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)
        #chat.controls.append(ft.Text(texto_entrou_chat))#add item to a list

        pagina.update()
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)


    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]#button from a list('[]')
        
    )

    def  abrir_popup(event):
        pagina.dialog = janela#'ll open->new'window
        janela.open = True#padron's try to open window locked->gotta tell to be open
        pagina.update()
        #print("Clicou no botão")

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

#main function of ur system
ft.app(main, view=ft.WEB_BROWSER)
#deploy
#site => (flet =>{deploy as web app})

#ctrl + c (on the terminal to stop)