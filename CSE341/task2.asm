
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
b db 6
          ; DATA SEGMENT .. FOR VARIABLES

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
    
    cmp bl,cl
    jg next  
    
    cmp cl,dl
    jg maximum_cl 
    
    mov ah,2 
    add dl,30h
    int 21h 
    jmp exit
    
    
    maximum_cl:
    mov ah,2
    mov dl,cl  
    add dl,30h
    int 21h 
    jmp exit
    
    next:
    cmp bl,dl
    jg final 
    mov ah,2 
    add dl,30h
    int 21h 
    jmp exit
    
    final:
    mov ah,2
    mov dl,bl
    add dl,30h
    int 21h
    
    
    
    
    
    
;    
    exit:
                 
;    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    