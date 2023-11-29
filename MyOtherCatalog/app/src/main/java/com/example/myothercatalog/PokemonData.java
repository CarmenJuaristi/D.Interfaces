package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class PokemonData {
    private String name;
    private String imageUrl;

    public PokemonData(String name, String imageUrl){
        this.name = name;
        this.imageUrl = imageUrl;
    }
    public String getName() {return name;}
    public String getImageUrl() {return imageUrl;}

    public PokemonData (JSONObject json){
        try{
            this.name = json.getString ("name");
            this.imageUrl = json.getString("imageUrl");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }
}
