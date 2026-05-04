import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portefólio - Renato Castro", layout="centered")

# Cabeçalho
st.title("👋 Renato G. Castro")
st.subheader("Vendedor de Loja")

# Sobre mim
st.header("📌 Sobre mim")
st.write("""
Sou vendedor de loja com experiência no atendimento ao cliente, vendas e organização de produtos.
Tenho interesse em tecnologia e estou a aprender Python para evoluir profissionalmente.
""")

# Competências
st.header("🛠 Competências")
st.write("""
- Atendimento ao cliente  
- Técnicas de venda  
- Organização de loja  
- Trabalho em equipa  
- Noções básicas de Python  
""")

# Experiência
st.header("💼 Experiência")
st.write("""
**Vendedor de Loja**  
- Atendimento direto ao cliente  
- Gestão de stock  
- Organização da loja  
- Fecho de caixa  
""")

# Contacto
st.header("📞 Contacto")
st.write("""
- Email: otanerortsac1@hotmail.com 
- Telemóvel: 965 889 612  
""")

# Rodapé
st.write("---")
st.write("Portefólio criado com Python + Streamlit")