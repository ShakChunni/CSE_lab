
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
var db ?
                ; DATA SEGMENT .. FOR VARIABLES ,string,array
msg db "Hello world!$"  ; last character of string is $

.CODE            

 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX
    lea dx,msg
    mov ah,9
    int 21h
    
   
     
    
            
    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    