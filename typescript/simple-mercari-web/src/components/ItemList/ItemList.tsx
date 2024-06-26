import React, { useEffect, useState } from 'react';

interface Item {
  id: number;
  name: string;
  category: string;
  image_name: string;
}

const server = process.env.REACT_APP_API_URL || 'http://127.0.0.1:9000';
const placeholderImage = process.env.PUBLIC_URL + '/logo192.png';

interface Prop {
  reload?: boolean;
  onLoadCompleted?: () => void;
}

export const ItemList: React.FC<Prop> = (props) => {
  const { reload = true, onLoadCompleted } = props;
  const [items, setItems] = useState<Item[]>([]);
  const fetchItems = () => {
    fetch(server.concat('/items'), {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('GET success:', data);
        setItems(data.items);
        onLoadCompleted && onLoadCompleted();
      })
      .catch((error) => {
        console.error('GET error:', error);
      });
  };

  const getImgSrc = (image_name: string) => {
    return image_name ? server.concat('/image/', image_name) : placeholderImage;
  };

  useEffect(() => {
    if (reload) {
      fetchItems();
    }
  }, [reload]);

  return (
    <div className="ItemList-Wrapper">
      {items.map((item) => {
        return (
          <div className="ItemContainer CircleAnimeBase" key={item.id}>
            <div className="ItemBg ItemList">
              <div className="ItemCategory">
                <span>{item.category}</span>
              </div>
            </div>
            <div className="ItemList">
              <img src={getImgSrc(item.image_name)} alt="item" />
              <p className="ItemName CircleAnimeTarget">
                <span>Name:</span>
                <span>{item.name}</span>
              </p>
            </div>
          </div>
        );
      })}
    </div>
  );
};
