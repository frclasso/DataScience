#!/usr/bin/env bash

##########################
#script shell para gnuplot
##########################

if [ $# -ne 3 ]
then
	echo "MODO DE USAR >> passe os seguintes parametros nesta ordem: funcao1 funcao2  nome_do_script"
	exit
fi

# passando o titulo para o parametro 3
echo "set title 'Grafico 1 - Ciências de Informação' " > $3
echo "set key above" >> $3
echo "set xlabel 'Coordenada X' " >> $3
echo "set ylabel 'Coordenada Y' " >> $3

# realizando o plot
echo "plot $1,$2" >> $3
