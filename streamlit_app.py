import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


g = 9.81 # gravidade [m/s^2]


st.title("UFRGS Portas Abertas")
st.title("A Matemática e o Lançamento de Foguetes")



st.header("Lançamento oblíquo") 

st.write("Entre os 3 tempos (segundos) e distâncias percorridas (metros) abaixo")


Tempo_1 = st.number_input("1o lançamento - tempo",
                          min_value=0.,
                          step = 0.01,
                          format = "%.2f",
                          label_visibility="visible"
                          )
Dist_1 = st.number_input("1o lançamento - distância",
                      min_value=0.,
                      step = 0.01,
                      format = "%.2f",
                      label_visibility="visible"
                      )

st.divider()

Tempo_2 = st.number_input("2o lançamento - tempo",
                          min_value=0.,
                          step = 0.01,
                          format = "%.2f",
                          label_visibility="visible"
                          )
Dist_2 = st.number_input("2o lançamento - distância",
                      min_value=0.,
                      step = 0.01,
                      format = "%.2f",
                      label_visibility="visible"
                      )

st.divider()

Tempo_3 = st.number_input("3o lançamento - tempo",
                          min_value=0.,
                          step = 0.01,
                          format = "%.2f",
                          label_visibility="visible"
                          )
Dist_3 = st.number_input("3o lançamento - distância",
                      min_value=0.,
                      step = 0.01,
                      format = "%.2f",
                      label_visibility="visible"
                      )

st.divider()



if st.button("Calcular"):

    # DISTÂNCIA E TEMPO
    Dist_max = max( Dist_1, Dist_2, Dist_3 )
    distancias = [Dist_1,Dist_2,Dist_3]
    tempos = [Tempo_1,Tempo_2,Tempo_3]
    for i in range(3):
        if Dist_max == distancias[i]:
            j = i
    Tempo = tempos[j]
    st.write("Maior distância: %.2f m"%Dist_max)
    st.write("Tempo da maior distância: %.2f s"%Tempo)

    # ANGULO
    Ang = np.arctan((g*Tempo**2-2)/(2*Dist_max))
    Ang_deg = np.degrees(Ang)
    st.write("Ângulo de lançamento: %.1fº"%Ang_deg)

    # VELOCIDADE
    Vel = Dist_max/(Tempo*np.cos(Ang))
    Vel_kmh = Vel*3.6
    st.write("Velocidade de lançamento: %.2f m/s = %.2f km/h"%(Vel,Vel_kmh))
    Vel_x = Vel*np.cos(Ang)
    Vel_y = Vel*np.sin(Ang)
    
    # ALTURA MÁXIMA ATINGIDA
    t1 = Vel_y/g
    Altura = 1+Vel_y**2/(2*g)
    st.write("Altura máxima atingida: %.2f m"%Altura)

    # GRAFICO
    fig,ax = plt.subplots()
    t = np.linspace(0,Tempo,100)
    x = Vel_x*t
    y = Vel_y*t - g*t*t/2 + 1
    ax.plot(x,y,color="blue")
    ax.grid()
    ax.set_xlabel(r"$x$ (m)")
    ax.set_ylabel(r"$y$ (m)")
    # ALTURA
    x0 = np.ones(2)*Vel_x*t1
    y0 = [0,Altura]
    ax.plot(x0,y0,color="black",linewidth="2")
    ax.text(Dist_max/2,Altura/2," %.2f"%Altura)
    # DISTANCIA MAXIMA
    x1 = [0,Dist_max]
    y1 = np.zeros(2)
    ax.plot(x1,y1,color="black",linewidth="2")
    ax.text(Dist_max/2,0,"%.2f"%Dist_max,
            verticalalignment="top",
            horizontalalignment="center"
            )
    # ANGULO
    Raio = Dist_max/5
    CompReta_y = Altura*.9
    ylim = ax.get_ylim()
    xlim = ax.get_xlim()
    xscale = xlim[-1] - xlim[0]
    yscale = ylim[-1] - ylim[0]
    thetascale = np.arctan(Vel_y/Vel_x*xscale/yscale)
    CompReta_x = CompReta_y/np.tan(Ang)
    x2=[CompReta_x,0,CompReta_x]
    y2=[1,1,1+CompReta_y]
    ax.plot(x2,y2,color="red",linewidth="1")
    Nscale = 20
    t3 = np.linspace(0,thetascale,Nscale)
    x3 = Raio*np.cos(t3)
    y3 = Raio*yscale/xscale*np.sin(t3)+1
    ax.plot(x3,y3,color="red",linewidth="1")
    ax.text(x3[Nscale//2],y3[Nscale//2],"%.1f°"%Ang_deg,
            verticalalignment="bottom",
            color="red"
            )
    #
    st.pyplot(fig)

    
    
    
    

# DESENVOLVIDO POR: MARCELO SCHRAMM E CIBELE LADEIA
st.divider()
st.caption("Desenvolvido por Marcelo Schramm e Cibele Aparecida Ladeia")




