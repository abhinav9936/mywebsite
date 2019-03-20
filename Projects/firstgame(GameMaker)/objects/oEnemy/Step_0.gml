
vsp = vsp + grv;

//horizontal Collision
if (place_meeting(x+hsp,y,oWall))//place_meeting checks for collisions
{
	while (!place_meeting(x+sign(hsp),y,oWall))//sign(hsp) returns 1 if hsp >0 and vice versa
	{
		x = x + sign(hsp);	
	}
	hsp = -hsp;
}
x = x + hsp;

//vertical collision
if (place_meeting(x,y+vsp,oWall))//place_meeting checks for collisions
{
	while (!place_meeting(x,y+sign(vsp),oWall))//sign(vsp) returns 1 if hsp >0 and vice versa
	{
		y = y + sign(vsp);	
	}
	vsp = 0;
}
y=y+vsp;

//Animation
if (!place_meeting(x,y+1,oWall))
{
	sprite_index = sEnemyA;
	image_speed = 0;
	if (sign(vsp)>0) image_index = 1; else image_index = 0;
}
else
{
	image_speed = 1;
	if (hsp == 0)
	{
		sprite_index = sEnemy;
	}
	else
	{
		sprite_index = sEnemyR;
	}
}
if(hsp !=0) image_xscale = sign(hsp)* size;
image_yscale = size;