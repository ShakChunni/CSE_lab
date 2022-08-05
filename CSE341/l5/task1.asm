
.MODEL SMALL 

.STACK 100H 

.DATA

arr1 db 1,2,3,4,5,6,7,8,9


.CODE            
 
MAIN PROC     
MOV AX,@DATA    
MOV DS,AX 
   mov ah,2
   mov si,1
   mov cx,4
   start:
   mov dl,arr1[si] 
   add dl,30h 
   int 21h
   add si,2
   loop start




    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    