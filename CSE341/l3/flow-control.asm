
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
b db 6
s dw "smaller$" 
g dw "greater$"          ; DATA SEGMENT .. FOR VARIABLES

.CODE            



 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX  



    mov bl,5
    ;sub bl,30h
    
    mov ah,1
    int 21h
    sub al,30h   ; al=3
    
    cmp al,bl   ; al=3, bl=5  ;jump less if al is less than bl
    JL here
    lea dx,g
    mov ah,9
    int 21h
    
    jmp exit 
    
    
    
    here:
    lea dx,s
    mov ah,9  
    int 21h  
    
    exit:
                 
;    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    