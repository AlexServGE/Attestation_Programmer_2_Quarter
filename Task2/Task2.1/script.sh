#!/bin/bash

mkdir -p toys_for_school_children/{Robots,Constructors,Table_games}.txt;
mkdir -p toys_for_preschool_children/{Soft_toys,Dolls,Cars}.txt;
mkdir Name_of_the_toy;
mv toys_for_{school,preschool}_children Name_of_the_toy;
mv Name_of_the_toy Toys;
ls -ali Toys;



