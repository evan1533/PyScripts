import textwrap



block  =[['0','W','E','R','T','1'],

             ['9','A','B','C','F','2'],

             ['8','H','I','J','K','3'],

             ['7','M','N','O','P','4'],

             ['6','U','V','X','Z','Q'],

             ['5','S','L','G','Y','D']];



def index_2d(myList, v):

    for i, x in enumerate(myList):

        if v in x:

            return (i, x.index(v))

        

def encrypt_text(s):

    index_array = [];

    top_string = "";

    bottom_string = "";

    for c in s:

        indx = index_2d(block,c);

        index_array.append(indx);

        top_string += str(indx[0]);

        bottom_string += str(indx[1]);

    combined_string = textwrap.wrap(top_string+bottom_string,2);


    encd_string = "";

    

    for elem in combined_string:

        ind_i = int(elem[0]);

        ind_j = int(elem[1]);

        encd_string += block[ind_i][ind_j];

    return encd_string;

        

def decrypt_text(s):

    index_array = [];

    comb_string = "";

    dec_string = "";

    for c in s:

        indx = index_2d(block,c);

        index_array.append(indx);

        comb_string += str(indx[0])+str(indx[1]);

    real_indx = textwrap.wrap(comb_string,1);

    indx_1 = real_indx[0:int((len(real_indx)/2))];

    indx_2 = real_indx[int((len(real_indx))/2):];

    for i in range(0,len(indx_1)):

        ind_i = int(indx_1[i]);

        ind_j = int(indx_2[i]);

        dec_string += block[ind_i][ind_j];

    return dec_string;
