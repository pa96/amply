set T;
set G;
# Definicion de parametro
param dem{t in T};
param c_ins{i in G};
param c_op{i in G};
# Definicion de variables
var xt{t in T}>=0;
var sit{i in G, t in T}>=0;
var yit{i in G, t in T}>=0;
var pt{t in T}>=0;
#Funcion objetivo
minimize Total_Cost:
sum{i in G, t in T}yit[i,t]*c_ins[i]+ sum{i in G, t in T}sit[i,t]*c_op[i]+ sum{t in T}pt[t]*70;
#Restricciones
subject to Cap_maxcomp{t in T}:
  xt[t]<=600;
subject to Cap_maxgen{i in G, t in T}:
  yit[i,t]<=100;
subject to Cap_mingen{i in G, t in T}:
  sit[i,t]>=yit[i,t]*0.75;
subject to Relacion{i in G, t in T}:
  sit[i,t]<=yit[i,t];
subject to Balance{t in T}:
  pt[t]=dem[t]-xt[t]-sum{i in G}sit[i,t];
