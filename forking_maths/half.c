#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv)
{
	printf("Process half has pid %d\n",getpid());
	if(argc <2 ){
		printf("Usage: twice integer\n");	
		exit(0);
	}

	sprintf(argv[argc-1],"%d",(atoi(argv[argc-1])/2));
	
	if(argc >2){
		char cwd[100];
		getcwd(cwd,sizeof(cwd));
		strcat(cwd,"/");
		strcat(cwd,argv[1]);
		argv[1]=cwd;
	}
	else
	{
		printf("the final result is %d\n",atoi(argv[argc-1]));
		return 0;
	}
	execvp(argv[1],argv+1);

}
