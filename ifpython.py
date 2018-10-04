    int regno[]={1,2,3,4,5};
    int regn,vote,counter,john=0,josp=0,eli=0,joy=0;
    for (counter=0;counter<5;counter++):
    {
    a:
    printf("Enter your voter registration number \n");
    scanf("%d",&regn);
    if (regn==regno[regn-1])
     {b:
     printf("Please enter the number of your candidate of choice \n");
     printf("1.John Mwangi\n2.Joseph Kaimuri\n3.Eliphas Kimundu\n4.Joy Muthengi\n");
     scanf("%d",&vote);
     if (vote>4 || vote<0)
        goto b;
    switch (vote)
    {
    case 1:
        john+=1;
        break;
    case 2:
        josp+=1;
        break;
    case 3:
        eli+=1;
        break;
    case 4:
        joy+=1;
        break;
    }
    regno[regn-1]=111;
    }
    else if (regno[regn-1]==111)
        {printf("You have already voted. You cannot vote twice \n");
        goto a;}
    else
    {printf("You do not qualify to vote \n");
        goto a;}}
    printf("These are the results of the elections \n");
    printf("******************************************** \n");
    printf("John Mwangi     : %d \n",john);
    printf("Joseph Kaimuri  : %d \n",josp);
    printf("Eliphas Kimundu : %d \n",eli);
    printf("Joy Muthengi    : %d \n",joy);
    printf("******************************************** \n\n\n");
    printf("******************************************** \n");
    if (john>josp && john>eli && john>joy)
        printf("\tJohn won the elections \n");
    if (josp>john && josp>eli && josp>joy)
        printf("\tJoseph won the elections \n");
    if (eli>josp && eli>john && eli>joy)
        printf("\tEli won the elections \n");
    if (joy>josp && joy>eli && joy>john)
        printf("\tJoy won the elections \n");
    else
    {
        if (john==josp && john+josp>eli+joy)
            printf("There will be a runoff between John and Joseph \n");
        if (john==eli && john+eli>josp+joy)
            printf("There will be a runoff between John and Eli \n");
        if (john==joy && john+joy>eli+josp)
            printf("There will be a runoff between John and Joy\n");
        if (eli==josp && eli+josp>john+joy)
            printf("There will be a runoff between Joseph and Eli\n");
        if (eli==joy && eli+joy>john+josp)
            printf("There will be a runoff between Eli and Joy \n");
        if (joy==josp && joy+josp>eli+john)
            printf("There will be a runoff between Joseph and Joy \n");
    }
    printf("******************************************** \n");
    return 0;
}
