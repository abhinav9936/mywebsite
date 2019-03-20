if(done == 0)
{

	vsp = vsp + grv;

	//horizontal Collision
	if (place_meeting(x+hsp,y,oWall))//place_meeting checks for collisions
	{
		while (!place_meeting(x+sign(hsp),y,oWall))//sign(hsp) returns 1 if hsp >0 and vice versa
		{
			x = x + sign(hsp);	
		}
		hsp = 0;
	}
	x = x + hsp;

	//vertical collision
	if (place_meeting(x,y+vsp,oWall))//place_meeting checks for collisions
	{
		if(vsp>0) 
		{
			done = 1;
			image_index = 1;
		}
		while (!place_meeting(x,y+sign(vsp),oWall))//sign(vsp) returns 1 if hsp >0 and vice versa
		{
			y = y + sign(vsp);	
		}
		vsp = 0;
	}
	y=y+vsp;
}
