package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class PokemonViewHolder extends RecyclerView.ViewHolder{
    private final TextView textView;
    private final ImageView imageView;
    public PokemonViewHolder (@NonNull View itemView){
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.pokemon_name_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.pokemon_image_view);
    }
    public void showData(PokemonData data, Activity activity){
        textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into (imageView);
    }
}
