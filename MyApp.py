import streamlit as st 
import pandas as pd 



# Crear un menú de navegación en la barra lateral
page = st.sidebar.radio("Página", 
["Inicio", "Acerca de", "Proyectos"])

def mostrar_inicio():
    st.markdown(
        """
        ## Quién es Andrés Felipe Bedoya Cruz

        Andrés Felipe Bedoya es un economista con experiencia en el uso de herramientas analíticas para analizar datos y en el área de la economía. Actualmente está cursando una maestría en analítica aplicada de datos con énfasis en gerencia y análisis prescriptivo. Tiene una formación profesional en economía y finanzas internacionales y ha trabajado como consultor e investigador en proyectos relacionados con la limpieza y transformación de bases de datos, el análisis descriptivo, el diseño y aplicación de algoritmos de clasificación de riesgo, el diseño de modelos econométricos y la evaluación del impacto de programas de salud. También ha desempeñado el cargo de auxiliar de investigación, donde ha apoyado en el desarrollo de modelos económicos y ha realizado análisis descriptivos y redacción de informes y presentaciones.
        """
     )
    # Mostrar información adicional

    st.write("LinkedIn: https://www.linkedin.com/in/andresbecr")
    st.write("twitter: @andresbecr")
    st.write("DeepNote: https://deepnote.com/@andresbecr")
    st.write("GitHub: https://github.com/andresbecr")
   


def mostrar_hoja_de_vida():
    # Crear un título para la hoja de vida
    st.title("Andrés Felipe Bedoya")


    # Mostrar información sobre tus habilidades y experiencia
    st.markdown(
        """
        ## Información personal

        Andrés Felipe Bedoya Cruz

        Bogotá, Colombia

        

        andres.f-7@hotmail.com

        linkedin.com/in/andresbecr

        ## Resumen

        Economista con experiencia en economía de la salud y en herramientas analíticas aplicadas a esta área. Formación profesional en economía y maestría en analítica aplicada de datos (cursando actualmente) con énfasis en gerencia y análisis prescriptivo.

        ## Habilidades

        * Excel (Power Query y Power Pivot)
        * Python
        * Stata
        * Power Bi
        * SQL (PostgreSQL)
        * VBA
        * Inglés B1

        ## Valores profesionales

        * Colaborador
        * Detallista
        * Analítico
        * Paciente

        ## Experiencia profesional

        ### Consultor e Investigador - Grupo ProyectaMe, Bogotá
        02/2020 - actualidad

        * Consulta, limpieza y transformación de bases datos.
        * Análisis descriptivo.
        * Diseño y aplicación de algoritmos de clasificación de riesgo en salud.
        * Diseño de modelos econométricos.
        * Evaluación de impacto en programas de salud.
        * Uso de herramientas para la visualización de datos.

        ### Auxiliar de investigación - Grupo ProyectaMe, Bogotá
        02/2019 - 02/2020

        * Apoyo en el proceso de desarrollo de modelos económicos de evaluaciones de tecnologías en salud, desde la discusión del diseño de la herramienta hasta el aporte en discusión y redacción de productos finales.
        * Análisis descriptivos que aportan en el diseño de modelos econométricos.
        * Redacción de informes y presentaciones.

        ## Formación académica

        ### Maestría en Analítica Aplicada (cursando) - Universidad de la Sabana
        2022

        ### Pregrado en Economía y Finanzas Internacionales - Universidad de la Sabana
        2013-2018
        """
    )


    # Mostrar información adicional

    st.write("LinkedIn: https://www.linkedin.com/in/mi-perfil")
    st.write("DeepNote: https://deepnote.com/@andresbecr")
    st.write("GitHub: https://github.com/andresbecr")

def mostrar_proyectos():
    st.markdown(
        """
        # Proyectos

        ## Discriminacion Salarial

        Descripción del proyecto 1...

        ## Delitos de alto impacto en la ciudad de Bogotá: Análisis mediante aprendizaje automatizado

        Visita  [DeepNote](https://deepnote.com/@andresbecr/ProyectoFinal-c2aca695-2adf-4ed3-85c4-a1c9c10a58e1) para ver el informe completo.
        
        
        ### Introducción
        Los delitos de alto impacto en la ciudad de Bogotá son una preocupación creciente para las autoridades y la población en general. Según cifras de la Secretaría Distrital de Seguridad, entre enero y agosto del 2021 se presentaron 65.207 casos de hurto a personas, un aumento de 12 mil casos en comparación con el año anterior en el mismo periodo. Además, una encuesta realizada por Invamer en abril del 2021 mostró que el 92,8% de los encuestados cree que la seguridad en la ciudad ha empeorado.

        En este contexto, se plantea el uso de aprendizaje automatizado para identificar y clasificar el tipo de delito de alto impacto ocurrido en la ciudad de Bogotá, con el fin de encontrar posibles relaciones entre las características del hecho delictivo y el mismo.

        ### Base de datos
        La base de datos utilizada en este estudio proviene de la Secretaría Distrital de Seguridad, Convivencia y Justicia de Bogotá. Incluye información sobre hechos delictivos denunciados en la ciudad de Bogotá durante el año 2017, agrupados por temporalidad, ubicación del delito y características del hecho. La base se actualiza mensualmente y está disponible en línea en el siguiente enlace: https://scj.gov.co/en/oficina-oaiee/estadisticas-mapas. Para el presente estudio se seleccionaron los delitos de mayor impacto, como hurto a personas, hurto a comercio, hurto de celulares, hurto a residencias, lesiones personales y violencia intrafamiliar. La base incluye un total de 168,628 instancias, con 7 atributos que describen el hecho delictivo, incluyendo tiempo, lugar y características del hecho. El objetivo es utilizar estos atributos para clasificar el tipo de delito mediante el uso de aprendizaje automatizado.

        ### Descripción
        Para el análisis, se excluyó la fecha del delito y la localidad de ocurrencia. La fecha se excluyó porque el objetivo del análisis no es predecir el tipo de delito en función del tiempo, sino encontrar relaciones entre las características del tiempo (rango del día, día de la semana y mes) y el tipo de delito. Por ejemplo, se puede esperar que la madrugada de un fin de semana en diciembre esté relacionada con un aumento en el número de hurtos a personas.

        La localidad de ocurrencia se excluyó y en su lugar se utilizó la UPZ (Unidad de Planeación Zonal), que es una agrupación más específica del lugar donde ocurrió el delito. Por sí sola, no se espera obtener una gran relación entre la UPZ y el tipo de delito, pero mediante esta característica se pueden unir otras características sociodemográficas relevantes como el nivel de pobreza, la calidad de vida, el ingreso per cápita, la densidad poblacional y el desempleo.

        ## 
        """
    )


# Mostrar el contenido de la página seleccionada en el menú
if page == "Inicio":
    mostrar_inicio()

elif page == "Acerca de":
    mostrar_hoja_de_vida()
elif page == "Proyectos":
    mostrar_proyectos()
