
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
b db 6
s dw "Smaller than 8$" 
e dw "It is 8$"
g dw "Greater than 8$"          ; DATA SEGMENT .. FOR VARIABLES

.CODE            



 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX   
    mov ah,1
    int 21h
    sub al,30h   
    mov bl,al 
     
    int 21h
    sub al,30h   
    mov cl,al 
   
    int 21h
    sub al,30h   
    mov dl,al  
    
    add bl,cl
    add dl,bl
    
    mov al,8
    cmp dl,al
    je equal
    
    
    
    
    cmp dl,al  
    jl less 
    
    lea dx,g
    mov ah,9
    int 21h
    jmp exit 
    
    less:
    lea dx,s
    mov ah,9
    int 21h 
    jmp exit 
    
    equal:
    lea dx,e
    mov ah,9
    int 21h
    jmp exit
    
    
    ;cmp al,bl  
;    JL here
;    
;    
;    jmp exit 
;    
;    
;    
;    here:
;    lea dx,s
;    mov ah,9  
;    int 21h  
;    
    exit:
                 
;    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    